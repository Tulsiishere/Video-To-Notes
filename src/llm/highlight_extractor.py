import json
import re
from pydantic import ValidationError
from src.llm.schema import VideoSummary
from src.llm.factory import get_llm
from src.logger import setup_logger

logger = setup_logger()

class HighlightExtractor:
    def __init__(self):
        self.llm = get_llm()

    def extract(self, prompt: str, output_path):
        logger.info("Calling LLM for highlights...")

        response = self.llm.generate(prompt)

        logger.debug(response)

        try:
            json_match = re.search(r"\{.*\}", response, re.DOTALL)

            if not json_match:
                logger.error("No JSON found in LLM response.")
                raise ValueError("Invalid LLM response format.")

            clean_json = json_match.group(0)

            data = json.loads(clean_json)
            
            validated = VideoSummary(**data)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(validated.dict(), f, indent=2)

            logger.info("Highlights extracted and validated.")
            return validated

        except (json.JSONDecodeError, ValidationError, ValueError) as e:
            logger.error("Invalid LLM response.")
            raise e