from langchain.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import CTransformers
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import pinecone
import os
import sys

DB_FAISS_PATH = "vectorstore/db_faiss"
#Read CSV files
loader = CSVLoader(file_path="Data/2019.csv",encoding="utf8",csv_args={'delimiter':','})
data=loader.load()
print(data)