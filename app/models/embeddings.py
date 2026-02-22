import os
from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")
BASE_URL = os.getenv("OLLAMA_BASE_URL")


def get_embeddings():
    """
    Returns Ollama embeddings model.
    Centralized config for reuse.
    """

    embeddings = OllamaEmbeddings(
        model=MODEL_NAME,
        base_url=BASE_URL
    )

    return embeddings