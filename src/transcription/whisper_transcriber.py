import whisper
import json
from pathlib import Path
from src.config import config
from src.logger import setup_logger

logger = setup_logger()

class WhisperTranscriber:
    def __init__(self):
        model_size = config.get("transcription", "model_size")
        device = config.get("transcription", "device")
        logger.info(f"Loading Whisper model: {model_size}")
        self.model = whisper.load_model(model_size, device=device)

    def transcribe(self, audio_path: Path, output_path: Path):
        logger.info("Starting transcription...")
        result = self.model.transcribe(str(audio_path))

        segments = [
            {
                "start": seg["start"],
                "end": seg["end"],
                "text": seg["text"].strip()
            }
            for seg in result["segments"]
        ]

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(segments, f, indent=2)

        logger.info("Transcription complete.")
        return segments