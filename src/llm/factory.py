import os
from src.config import config
#from src.llm.openai_client import OpenAIClient
from src.llm.gemini_client import GeminiClient
"""
def get_llm(provider="gemini"):

    if provider == "openai":
        return OpenAIClient()
    elif provider == "gemini":
        return GeminiClient()
    else:
        raise ValueError("Unsupported LLM provider: {provider}")
"""

def get_llm():
    return GeminiClient(model="gemini-2.5-flash")