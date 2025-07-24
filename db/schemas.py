from pydantic import BaseModel

class FeedbackCreate(BaseModel):
    student_id: str
    subject: str
    score: float
    comments: str

class FeedbackResponse(FeedbackCreate):
    id: int

    class Config:
        orm_mode = True
