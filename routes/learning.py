# routes/learning.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db.database import get_db
from utils.llm_question_generator import generate_llm_questions
from sqlalchemy.orm import Session
from models import User, LearningTrack, Question  # adjust import if needed

router = APIRouter()

class StartLearningRequest(BaseModel):
    user_id: int
    topic: str

@router.post("/start-learning")
def start_learning(request: StartLearningRequest):
    db: Session = get_db()

    user = db.query(User).filter(User.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # 1. Create learning track
    track = LearningTrack(user_id=request.user_id, topic=request.topic)
    db.add(track)
    db.commit()
    db.refresh(track)

    # 2. Generate questions using Gemini
    questions_data = generate_llm_questions(request.topic)
    if not questions_data:
        raise HTTPException(status_code=500, detail="LLM failed to generate questions")

    # 3. Save questions
    for q in questions_data:
        new_q = Question(
            track_id=track.id,
            question=q["question"],
            options=q["options"],
            answer=q["answer"],
            level=q["level"]
        )
        db.add(new_q)

    db.commit()

    return {"track_id": track.id, "questions_created": len(questions_data)}
