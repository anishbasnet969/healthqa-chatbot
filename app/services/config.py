import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
DOCUMENTS_PATH = os.path.join(BASE_DIR, "documents")
CHROMA_PATH = os.path.join(BASE_DIR, "chroma_db")

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

EMBEDDING_MODEL = "models/text-embedding-004"
LLM_MODEL = "gemini-2.0-flash"
TEMPERATURE = 0
