from pydantic import BaseModel
from typing import Optional,List

class UserCreate(BaseModel):
    name: str

class QuestionResponse(BaseModel):
    question_id: int
    question: str

class AnswerSubmit(BaseModel):
    user_id: int
    question_id: int
    user_answer: str

class FeedbackSubmit(BaseModel):
    user_id: int
    comment: str

class QuestionCreate(BaseModel):
    question: str
    choices: List[str]
    correct_answer: str
    difficulty: float
class QuestionUpdate(BaseModel):
    question_id: int
    question: str
    choices: List[str]
    correct_answer: str
    difficulty: float
class DashboardResponse(BaseModel):
    user_id: int
    ability: float
    accuracy: float
    feedback_summary: str
