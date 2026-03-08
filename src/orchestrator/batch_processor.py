from pathlib import Path
from src.pipeline.processor import process_video
from src.logger import setup_logger

logger = setup_logger()


def process_batch(input_dir: Path):
    """
    Process all videos inside input directory.
    Each video is isolated — one failure won't stop others.
    """
    videos = list(input_dir.glob("*.mp4"))

    if not videos:
        logger.warning("No videos found.")
        return

    logger.info(f"Found {len(videos)} video(s)")

    for video in videos:
        logger.info(f"\nProcessing: {video.name}")

        try:
            process_video(video)
            logger.info(f"Completed: {video.name}")
        except Exception as e:
            logger.error(f"Failed: {video.name}")
            logger.error(str(e))
            continue