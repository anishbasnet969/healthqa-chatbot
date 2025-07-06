from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.callbacks import BaseCallbackHandler

import os
from app.services.config import DOCUMENTS_PATH


class PromptPrinterCallback(BaseCallbackHandler):
    """Simple callback to log the prompt being sent to the LLM"""

    def on_llm_start(self, serialized, prompts, **kwargs):
        print("\n" + "=" * 80)
        print("PROMPT BEING SENT TO LLM:")
        print("=" * 80)
        for i, prompt in enumerate(prompts):
            print(f"Prompt {i+1}:")
            print(prompt)
            print("-" * 80)
        print("=" * 80 + "\n")


def load_documents():
    docs = []
    for filename in os.listdir(DOCUMENTS_PATH):
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DOCUMENTS_PATH, filename))
            loaded = loader.load()
            for doc in loaded:
                doc.metadata["source"] = (
                    filename  # Adding filename as the source of document to metadata
                )
            docs.extend(loaded)
    return docs


def split_documents(docs, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(docs)
