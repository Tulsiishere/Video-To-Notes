import os
import subprocess
from pathlib import Path
from src.logger import setup_logger

logger = setup_logger()


class ClipGenerator:
    def __init__(self, video_path: Path, output_dir: Path):
        self.video_path = str(video_path)
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_clip(self, start: int, end: int, filename: str):
        output_path = self.output_dir / filename

        command = [
            "ffmpeg",
            "-y",
            "-i", self.video_path,
            "-ss", str(start),
            "-to", str(end),
            "-c", "copy",
            str(output_path)
        ]

        try:
            subprocess.run(
                command,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            logger.info(f"Clip created: {output_path}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Clip generation failed: {e}")

    def generate_from_summary(self, summary_data):
        """
        summary_data is your validated Pydantic object
        """
        for idx, highlight in enumerate(summary_data.highlights, start=1):

            start = highlight.start_time_seconds
            end = highlight.end_time_seconds

            safe_title = "".join(
                c for c in highlight.title if c.isalnum() or c in (" ", "_")
            ).replace(" ", "_").lower()

            filename = f"clip_{idx}_{safe_title[:30]}.mp4"

            self.generate_clip(start, end, filename)