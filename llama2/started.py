from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.embeddings import resolve_embed_model
from llama_index.llms import Ollama
import os
import logging
import sys

##logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
#logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

import openai

import os
import sys
import getpass

os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')

##Sprint(os.listdir())
documents = SimpleDirectoryReader("/Users/lrao9/Desktop/GenAi-Using-LangChain/LangChain/data/RAG/").load_data()

# bge-m3 embedding model
embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")

# ollama
llm = Ollama(model="mistral", request_timeout=30.0)

service_context = ServiceContext.from_defaults(
    embed_model=embed_model, llm=llm
)

index = VectorStoreIndex.from_documents(
    documents, service_context=service_context
)

query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)