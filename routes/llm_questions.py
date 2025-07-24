from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils.llm_question_generator import generate_llm_questions
from db.database import SessionLocal
from models.models import Question

router = APIRouter()

class TopicRequest(BaseModel):
    topic: str
    user_id: int

@router.post("/generate-questions/")
def generate_questions(req: TopicRequest):
    try:
        questions = generate_llm_questions(req.topic)
        db = SessionLocal()
        for q in questions:
            new_question = Question(
                topic=req.topic,
                level="easy",  # You can enhance with difficulty logic
                content=q["question"],
                correct_answer=q["answer"],
                options=q["options"],
                user_id=req.user_id
            )
            db.add(new_question)
        db.commit()
        db.close()
        return {"message": "Questions generated and saved"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
