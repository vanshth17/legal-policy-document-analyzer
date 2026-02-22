import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")
BASE_URL = os.getenv("OLLAMA_BASE_URL")


def get_llm():
    """
    Central LLM loader.
    Keeps configuration secure and reusable.
    """
    llm = ChatOllama(
        model=MODEL_NAME,
        base_url=BASE_URL,
        temperature=0
    )
    return llm
