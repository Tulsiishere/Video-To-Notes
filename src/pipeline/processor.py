from pathlib import Path
from src.media.audio_extractor import extract_audio
from src.transcription.whisper_transcriber import WhisperTranscriber
from src.utils.chunker import chunk_transcript
from src.llm.prompt_builder import build_highlight_prompt
from src.llm.highlight_extractor import HighlightExtractor
from src.markdown.builder import build_markdown
from src.config import config
from src.video.clip_generator import ClipGenerator
from src.media.screenshot_extractor import extract_screenshot

def process_video(video_path: Path):

    video_name = video_path.stem
    output_root = Path(config.get("paths", "output_root")) / video_name

    audio_path = Path("temp") / f"{video_name}.wav"
    transcript_path = output_root / "transcript.json"
    highlights_path = output_root / "highlights.json"
    markdown_path = output_root / "Summary.md"

    # Extract audio
    extract_audio(video_path, audio_path)

    # Transcribe
    transcriber = WhisperTranscriber()
    segments = transcriber.transcribe(audio_path, transcript_path)

    # Chunk
    chunk_minutes = config.get("chunking", "chunk_minutes")
    chunks = chunk_transcript(segments, chunk_minutes)

    # LLM
    prompt = build_highlight_prompt(chunks)
    extractor = HighlightExtractor()
    summary_data = extractor.extract(prompt, highlights_path)
    # Screenshot Extraction
    screenshots_dir = output_root / "screenshots"
    for idx, highlight in enumerate(summary_data.highlights, start=1):
        midpoint = (highlight.start_time_seconds + highlight.end_time_seconds) / 2
        screenshot_path = screenshots_dir / f"highlight_{idx}.png"
        extract_screenshot(video_path, midpoint, screenshot_path)

    # Clip Generator
    clips_dir = output_root / "clips"
    clipper = ClipGenerator(video_path, clips_dir)
    clipper.generate_from_summary(summary_data)

    # Markdown
    build_markdown(video_name, summary_data, markdown_path)

    print(f"Processing complete for {video_name}")