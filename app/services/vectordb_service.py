from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.services.utils import load_documents, split_documents
from app.services.config import EMBEDDING_MODEL, CHROMA_PATH

import os

embeddings = GoogleGenerativeAIEmbeddings(
    model=EMBEDDING_MODEL, google_api_key=os.getenv("GOOGLE_API_KEY")
)


def get_vectorstore():
    os.makedirs(CHROMA_PATH, exist_ok=True)
    docs = load_documents()
    split_docs = split_documents(docs)
    vectordb = Chroma.from_documents(
        split_docs, embeddings, persist_directory=CHROMA_PATH
    )
    return vectordb


def load_vectorstore():
    if not os.path.exists(CHROMA_PATH) or not os.listdir(CHROMA_PATH):
        raise ValueError("Vectorstore not found or is empty.")
    vectordb = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
    return vectordb
