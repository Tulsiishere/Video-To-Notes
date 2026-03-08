from dotenv import load_dotenv
from pathlib import Path
from src.orchestrator.batch_processor import process_batch

load_dotenv()

if __name__ == "__main__":
    videos_folder = Path("input/videos")
    process_batch(videos_folder)