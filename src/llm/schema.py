from pydantic import BaseModel, Field
from typing import List

class Highlight(BaseModel):
    title: str
    start_time_seconds: float
    end_time_seconds: float
    why_important: str
    key_points: List[str]
    action_items: List[str]
    confidence_score: float = Field(ge=0.0, le=1.0)

class VideoSummary(BaseModel):
    video_summary: str
    highlights: List[Highlight]
    overall_takeaways: List[str]