import subprocess
from pathlib import Path
from src.logger import setup_logger

logger = setup_logger()


def extract_screenshot(video_path: Path, timestamp: float, output_path: Path):
    """
    Extract a single screenshot from video at a given timestamp.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    command = [
        "ffmpeg",
        "-y",
        "-ss", str(timestamp),
        "-i", str(video_path),
        "-frames:v", "1",
        "-q:v", "2",   # good quality
        str(output_path)
    ]

    logger.info(f"Extracting screenshot at {timestamp} seconds")

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if not output_path.exists():
        logger.error(result.stderr)
        raise RuntimeError("Screenshot extraction failed.")

    logger.info("Screenshot saved.")