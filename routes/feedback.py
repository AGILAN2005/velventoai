from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from models.models import Feedback, Summary
from schemas.schemas import FeedbackSubmit
from utils.gemini_rag import generate_summary

router = APIRouter()

@router.post("/submit-feedback")
def submit_feedback(data: FeedbackSubmit, db: Session = Depends(get_db)):
    feedback = Feedback(user_id=data.user_id, comment=data.comment)
    db.add(feedback)
    db.commit()

    summary_text = generate_summary(data.comment)
    summary = Summary(user_id=data.user_id, summary_text=summary_text)
    db.add(summary)
    db.commit()
    return {"summary": summary_text}
