<img width="545" alt="image" src="https://github.com/klnsuman/LangChain/assets/11458777/5e28fec4-d192-47bd-b57d-cd28f3d07d82">


```diff
- 1. LLM
  LLM is the fundamental component of LangChain. It is a wrapper around the large language model which enables in utilization
  of the functionalities and capabilities of the model.
+ 2. Chains
  One single call to LLM Would not be enough. This module allows other tools to be integrated.
 
  Ex:Get data from a specific URL, summarize the returned text, and answer questions using the generated summary. 
      This module allows multiple tools to be concatenated in order to solve complex tasks

- 3. Prompts
  Prompts are at the core of any NLP application. It is how users interact with the model to try and obtain an output from it.
+ 4. Document Loaders and Utils
  LLM can connect to external sources like , pdf , epub , word document ,text file etc and expand their knowlodge and answer relevant questions

- 5. Agents :
    Helps LLM to interact with its environment and take decisions.
    For Ex : if we command to create a dataframe and perform analysis. LLM internall invokes python repl function and invokes pandas library to create pandas dataframe.
             Also calls matplotlib library to make graphs.
- 6. Indexes - Vector Databases (Indexes):
      Converts text to embeddings and stores these embeddings in vector databases for search and retrieval using RAG. Similarity Search.
- 7. Memory
      This module enables users to create a persisting state between calls of a model.
```


----------------------------------------------------------------------
<Body>
<h1 style="color:blue;">Basic Topics</h1> 

Notebook | Description
:- | :-
[LLM_1.ipynb](https://github.com/klnsuman/LangChain/blob/main/LLM_1.ipynb) | Simple LLM - Similar to hellow world program. Use LLM OpenAI to Pedict.
[Prompts_LangChain.ipynb](https://github.com/klnsuman/LangChain/blob/main/Prompts_LangChain.ipynb) | Usage of Prompts , Prompt Templates,output parser
[Ques-and-Ans_DocumentLoaders.ipynb](https://github.com/klnsuman/LangChain/blob/main/QA_DocumentLoaders_Langchain.ipynb) | Text Loaders , Csv Loaders
[Streamlit-Basic.ipynb](https://github.com/klnsuman/LangChain/blob/main/Streamlit_sample.ipynb) | Executing Streamlit from google colab
[LangChain-ChatMessages.ipynb](https://github.com/klnsuman/LangChain/blob/main/LangCain_ChatMessages.ipynb)| Demo of using Chat Models and Messages using Lang Chain
[Embeddings_LangChain.ipynb](Embeddings_LangChain.ipynb)| Generate Text Embeddings using OpenAI Enbeddings
[Agents_SerpAPI.ipynb]([Agents_SerpAPI.ipynb](https://github.com/klnsuman/LangChain-Dissertation-Using-CodeSpaces/tree/main/Chat_With_Retrieval))| Notebook Contains Integrate with Google Search , Execute SQL Query , FAISS Vector DB , ChatBots with Memory


<h1 style="color:blue;">Advanced Topics</h1>

Notebook | Description
:- | :-
[chat_with_documents.py](chat_with_documents.py) | Chat with PDF Documents.

</Body>


