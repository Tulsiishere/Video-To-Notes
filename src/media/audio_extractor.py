import subprocess
from pathlib import Path
from src.logger import setup_logger

logger = setup_logger()

def extract_audio(video_path: Path, output_path: Path) -> Path:
    """
    Extracts audio from video using FFmpeg.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    command = [
        "ffmpeg",
        "-y",
        "-i", str(video_path),
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        str(output_path)
    ]

    logger.info(f"Extracting audio from {video_path.name}")

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        logger.error("FFmpeg error:")
        logger.error(result.stderr)
        raise RuntimeError("Audio extraction failed.")

    if not output_path.exists():
        raise RuntimeError("Audio file was not created.")

    logger.info("Audio extraction complete.")
    return output_path