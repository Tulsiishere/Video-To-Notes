# Video-to-Notes AI Platform

## Sections
1. Project Overview
2. System Architecture
3. Pipeline Workflow
4. Features
5. Tech Stack
6. Installation
7. Usage
8. Example Output
9. Future Improvements

## Project Overview

Video-to-Notes AI is an AI-powered system that converts long-form videos into structured, readable notes using speech recognition and large language models.

The platform is designed to process long-duration videos (3–4 hours, 200MB+) and automatically generate a structured knowledge package that includes:

- Summary.md – Structured notes with timestamps

- Highlight video clips

- Important screenshots

- Organized output folders per video

This system demonstrates how Generative AI pipelines can transform unstructured multimedia content into structured knowledge artifacts.

------------------------------------------------------------------------

## System Architecture

The project follows a modular AI pipeline architecture.

```
video-to-notes-ai/
│
├── config/                     # Configuration files
│
├── input/                      # Input data
│   └── videos/                 # Raw videos to process
│
├── logs/                       # Application logs
│
├── output/                     # Generated outputs
│   └── <video_name>/
│       ├── Summary.md
│       ├── clips/
│       └── screenshots/
│
├── src/                        # Core application source code
│
│   ├── llm/                    # LLM abstraction layer
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── factory.py
│   │   ├── gemini_client.py
│   │   ├── openai_client.py
│   │   ├── highlight_extractor.py
│   │   ├── prompt_builder.py
│   │   └── schema.py
│
│   ├── markdown/               # Markdown generation
│   │   ├── __init__.py
│   │   └── builder.py
│
│   ├── media/                  # Media processing utilities
│   │   ├── __init__.py
│   │   ├── audio_extractor.py
│   │   └── screenshot_extractor.py
│
│   ├── orchestrator/           # Batch execution manager
│   │   └── batch_processor.py
│
│   ├── pipeline/               # Core AI pipeline logic
│   │   └── processor.py
│
│   ├── transcription/          # Speech-to-text modules
│   │   ├── __init__.py
│   │   └── whisper_transcriber.py
│
│   ├── utils/                  # Utility functions
│   │   ├── __init__.py
│   │   └── chunker.py
│
│   ├── video/                  # Video clip generation
│   │   ├── __init__.py
│   │   └── clip_generator.py
│
│   ├── config.py               # Global configuration loader
│   └── logger.py               # Logging configuration
│
├── temp/                       # Temporary processing files
│
├── .env                        # Environment variables (API keys)
├── main.py                     # Application entry point
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

The system processes each video independently and generates a complete output package.

------------------------------------------------------------------------

## Pipeline Workflow

The system processes videos through a multi-stage AI pipeline:

**Step 1 — Audio Extraction**

Audio is extracted from the input video using FFmpeg.

**Step 2 — Transcription**

Speech is converted into text using Whisper (local or API).

**Step 3 — LLM Summarization**

The transcript is processed by an LLM to generate:

* High-level summary
* Timestamped highlights
* Key insights
* Actionable points

**Step 4 — Asset Extraction**

Important moments from the video are extracted as:

* Short highlight clips
* Screenshots aligned to timestamps

**Step 5 — Markdown Generation**

All outputs are compiled into a structured Markdown document (`Summary.md`) linking transcripts, clips, and screenshots.

The system runs in batch mode, processing all videos placed inside:

`input/videos/`

------------------------------------------------------------------------

## Features

* Handles large long-duration videos (200MB+)
* Batch processing for multiple videos
* Accurate timestamps across notes and media
* Generates structured Markdown documentation
* Extracts highlight clips and screenshots
* Designed with modular AI pipeline architecture
* Easily extensible for cloud deployment or web applications

------------------------------------------------------------------------

## Tech Stack

**Programming Language**
* Python

**AI / Machine Learning**
* Whisper (Speech Recognition)
* OpenAI GPT
* Google Gemini

**Media Processing**
* FFmpeg
* MoviePy

**Utilities**
* Python Dotenv
* YAML Configuration

------------------------------------------------------------------------

## Installation

Clone the repository:

```
git clone https://github.com/Tulsiishere/Video-To-Notes.git
cd Video-To-Notes
```

Install dependencies:

```
pip install -r requirements.txt
```

Install FFmpeg and ensure it is available in the system PATH.

------------------------------------------------------------------------

## Usage

**Step 1 — Set API Keys**

Set the required environment variables.

* OpenAI
    ```export OPENAI_API_KEY="your_key_here"```

* Google Gemini

    ```export GEMINI_API_KEY="your_key_here"```

* Windows PowerShell:

    ```setx OPENAI_API_KEY "your_key_here"``` 
    ```setx GEMINI_API_KEY "your_key_here"```

**Step 2 — Add Input Videos**

Place videos inside:

`input/videos/`

**Step 3 — Run the Pipeline**
`python main.py`

**Step 4 — View Results**

The generated results will appear in:

`output/<video_name>/`

Each processed video will include:
* Summary.md
* clips/
* screenshots/

------------------------------------------------------------------------

## Example Output

Example generated structure:

```
output/
  AI_Lecture_01/
    Summary.md
    clips/
      highlight_1.mp4
      highlight_2.mp4
    screenshots/
      frame_01.png
      frame_02.png
```

Example section from Summary.md:

```
## Key Concepts

00:15:32 — Introduction to Neural Networks  
01:04:10 — Gradient Descent Explained  
02:22:45 — Practical Training Example
```

This allows users to quickly navigate long videos through structured knowledge summaries.

------------------------------------------------------------------------

## Future Improvements

Planned improvements for the platform include:

* Web-based interface for uploading videos
* Interactive video navigation through timestamps
* Retrieval-Augmented Generation (RAG) for long transcripts
* Export notes to PDF / DOCX
* Cloud deployment for large-scale processing
* Support for YouTube and online video sources
* Semantic search across generated notes
