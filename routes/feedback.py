from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from db import models, schemas
from rag.chroma_db import add_feedback_to_vector_db

router = APIRouter()

@router.post("/submit-feedback", response_model=schemas.FeedbackResponse)
def submit_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    db_feedback = models.Feedback(
        student_id=feedback.student_id,
        subject=feedback.subject,
        score=feedback.score,
        comments=feedback.comments
    )
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)

    # ✅ Add to ChromaDB for RAG use
    try:
        add_feedback_to_vector_db(student_id=feedback.student_id, feedback_text=feedback.comments)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"ChromaDB error: {str(e)}")

    return db_feedback
