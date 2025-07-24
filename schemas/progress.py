from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProgressCreate(BaseModel):
    student_id: str
    question: str
    answer: str
    score: float
    feedback: Optional[str] = None

class ProgressResponse(ProgressCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
