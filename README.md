# Enhancing-Question-Answering-with-Knowledge-Graph-Retrieval-and-Generation-Using-LLM
# Objective:
The main objective of the GRAG project was to develop a novel approach that combines the strengths of Knowledge Graphs and Large Language Models (LLMs) to enhance the performance of natural language processing tasks, such as text summarization and question answering, while maintaining efficiency and scalability.

# Approach:
The GRAG approach involves the following main components:

### Knowledge Graph Construction:
A Knowledge Graph was constructed by ingesting and structuring information from various sources, including Form 10-K reports obtained from the EDGAR database maintained by the UNITED STATES SECURITIES AND EXCHANGE COMMISSION.

![image](https://github.com/supraj221/Enhancing-Question-Answering-with-Knowledge-Graph-Retrieval-and-Generation-Using-LLM-/assets/92993235/464d11ad-abad-4778-86ff-75ec7f4f9047)

Fig Flowchart of Knowledge Graph Creation

![image](https://github.com/supraj221/Enhancing-Question-Answering-with-Knowledge-Graph-Retrieval-and-Generation-Using-LLM-/assets/92993235/69b5e2c1-bf72-4701-af79-a007c9d9da2e)

Fig Next Relation

![image](https://github.com/supraj221/Enhancing-Question-Answering-with-Knowledge-Graph-Retrieval-and-Generation-Using-LLM-/assets/92993235/b4e37f21-faf4-4cdb-b9ac-ebe38887b174)

Fig Section Relation

![image](https://github.com/supraj221/Enhancing-Question-Answering-with-Knowledge-Graph-Retrieval-and-Generation-Using-LLM-/assets/92993235/22422508-41c6-42b9-a9ba-106d67332696)

Fig Part_Of Relation

![image](https://github.com/supraj221/Enhancing-Question-Answering-with-Knowledge-Graph-Retrieval-and-Generation-Using-LLM-/assets/92993235/0fb194a4-0d18-48e8-91f2-bfb77dbeabb5)

Fig Intersection of All Relations

### Retrieval Module: 
A hybrid retrieval scheme was developed, combining vector similarity and graph-based associations to retrieve relevant information from the Knowledge Graph based on the input text or query.
### Language Model Integration: 
Large Language Models (LLMs), such as PaLM 2 and Text BISON, were integrated into the GRAG system to leverage their powerful language understanding and generation capabilities.
### Retrieval Augmentation: 
The retrieved information from the Knowledge Graph was used to augment the prompts or inputs provided to the LLM, enabling the generation of more accurate and context-aware responses.

## UI:
![image](https://github.com/supraj221/Enhancing-Question-Answering-with-Knowledge-Graph-Retrieval-and-Generation-Using-LLM-/assets/92993235/7a7fc59b-1177-4449-8325-b0fbbea28204)

Fig Response of First Question

![image](https://github.com/supraj221/Enhancing-Question-Answering-with-Knowledge-Graph-Retrieval-and-Generation-Using-LLM-/assets/92993235/eb9fec66-756f-47b0-9c96-e2b4f629d42d)

Fig Response of Second Question

![image](https://github.com/supraj221/Enhancing-Question-Answering-with-Knowledge-Graph-Retrieval-and-Generation-Using-LLM-/assets/92993235/ed3d36aa-aa60-4475-adc4-1e1002b85a10)

Fig Response of Third Question


