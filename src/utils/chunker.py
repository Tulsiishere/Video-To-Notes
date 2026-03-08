from typing import List, Dict

def chunk_transcript(segments: List[Dict], chunk_minutes: int):
    """
    Groups transcript segments into time-based chunks.
    """
    chunk_seconds = chunk_minutes * 60
    chunks = []
    current_chunk = []
    current_start = segments[0]["start"]

    for seg in segments:
        if seg["end"] - current_start <= chunk_seconds:
            current_chunk.append(seg)
        else:
            chunks.append(current_chunk)
            current_chunk = [seg]
            current_start = seg["start"]

    if current_chunk:
        chunks.append(current_chunk)

    return chunks