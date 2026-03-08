import google.generativeai as genai
from src.llm.base import BaseLLM
from src.logger import setup_logger
import os

logger = setup_logger()

class GeminiClient(BaseLLM):

    def __init__(self, model="gemini-2.5-flash"):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not set in environment.")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)

    def generate(self, prompt: str) -> str:
        logger.info("Calling Gemini LLM...")
        response = self.model.generate_content(prompt)
        return response.text