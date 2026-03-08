import json

def build_highlight_prompt(chunks):
    """
    Builds strict prompt for structured JSON output.
    """

    transcript_text = ""

    for chunk in chunks:
        for seg in chunk:
            transcript_text += f"[{seg['start']:.2f} - {seg['end']:.2f}] {seg['text']}\n"

    prompt = f"""
You are an AI assistant that extracts structured highlights from a video transcript.

STRICT RULES:
- Use ONLY timestamps present in transcript.
- Do NOT invent timestamps.
- Return STRICT JSON only.
- Max 12 highlights.
- Each highlight must be between 30 and 180 seconds.
-Do not include markdown formatting in the highlights.
-Do not include explanations in the highlights.
_ Do not wrap the json in ```json blocks.

Return JSON matching this structure:
{{
  "video_summary": "string",
  "highlights": [
    {{
      "title": "string",
      "start_time_seconds": number,
      "end_time_seconds": number,
      "why_important": "string",
      "key_points": ["string"],
      "action_items": ["string"],
      "confidence_score": number
    }}
  ],
  "overall_takeaways": ["string"]
}}

Transcript:
{transcript_text}
"""

    return prompt