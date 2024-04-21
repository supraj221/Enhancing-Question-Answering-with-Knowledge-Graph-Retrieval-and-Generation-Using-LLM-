import streamlit as st
from google.cloud import secretmanager
import vertexai
import warnings
import os
from langchain_community.graphs import Neo4jGraph
import vertexai
from vertexai.language_models import TextGenerationModel

NEO4J_URI = ""
NEO4J_USERNAME = ""
NEO4J_PASSWORD = ""
NEO4J_DATABASE = ""

# Langchain
from langchain_community.graphs import Neo4jGraph
from langchain_community.vectorstores import Neo4jVector

with warnings.catch_warnings():
    warnings.simplefilter('ignore')

def access_secret_version(secret_version_id):
  client = secretmanager.SecretManagerServiceClient()
  response = client.access_secret_version(name=secret_version_id)
  return response.payload.data.decode('UTF-8')

secret_version_id = f""

key=access_secret_version(secret_version_id)
os.getenv(key)

vertexai.init(project='', location='')

VECTOR_INDEX_NAME = 'form_10k_chunks'
VECTOR_NODE_LABEL = 'Chunk'
VECTOR_SOURCE_PROPERTY = 'text'
VECTOR_EMBEDDING_PROPERTY = 'textEmbedding'

kg = Neo4jGraph(
    url=NEO4J_URI, username=NEO4J_USERNAME, password=NEO4J_PASSWORD, database=NEO4J_DATABASE
)

def neo4j_vector_search(question):
  vector_search_query = """
    WITH genai.vector.encode(
      $question,
      "VertexAI",{
      token: "", 
      projectId: ''
      })
      AS question_embedding
    CALL db.index.vector.queryNodes($index_name, $top_k, question_embedding) yield node, score
    RETURN score, node.text AS text,node.chunkId as chunkId
  """
  similar = kg.query(vector_search_query,
                     params={
                      'question': question,
                      'index_name':VECTOR_INDEX_NAME,
                      'top_k': 1})
  return similar

def get_top_node_and_next_two(question):
    # Perform vector similarity search to get the top-1 node
    top_node_result = neo4j_vector_search(question)

    # Extract the chunkId of the top-1 node
    top_node_chunk_id = top_node_result[0]['chunkId']

    # Query to get the text of the top node and the next two nodes
    query = """
    MATCH (start:Chunk {chunkId: $chunk_id})
    MATCH path = (start)-[:NEXT*0..2]-(next)
    WITH start, [n IN nodes(path) WHERE n <> start] AS nextNodes
    RETURN start.text + ' ' + REDUCE(s = '', n IN nextNodes | s + n.text + ' ') AS concatenatedText
    """
    

    # Execute the query with the top node's chunkId
    result = kg.query(query, params={'chunk_id': top_node_chunk_id})


    # Return the concatenated text
    return result[-1]['concatenatedText'], top_node_result[0]


def interview(
    temperature: float,
    project_id: str,
    location: str,
    question: str,
    context: str,
    template: str,
) -> str:
    """Ideation example with a Large Language Model"""

    vertexai.init(project=project_id, location=location)
    # developer - override these parameters as needed:
    parameters = {
        "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
        "top_p": 0.8,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }

    model = TextGenerationModel.from_pretrained("text-bison@002")
    prompt = template.format(context=context, question=question)
    response = model.predict(
        prompt,
        **parameters,
    )
    print(f"Response from Model: {response.text}")

    return response.text

    
def main():
    st.title("Knowledge Graph Chatbot")
    user_question = st.text_input("Ask a question:")
    submit_button = st.button("Submit")

    if submit_button and user_question:
        context, top_result = get_top_node_and_next_two(user_question)
        template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. {context} Question: {question} Helpful Answer:"""

        response = interview(
            temperature=0.0,
            project_id='',
            location='',
            question=user_question,
            context=context,
            template=template,
        )

        # Get the score from the top_result
        score = top_result['score']

        st.write(f"Response: {response}")
        st.write(f"Score: {score:.2f}")



if __name__ == "__main__":
    main()