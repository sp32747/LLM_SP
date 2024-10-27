import os
import streamlit as st
import pickle
import time
import langchain
from langchain_openai import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

openai_api_key =os.environ.get("OPENAI_API_KEY")
print(openai_api_key)