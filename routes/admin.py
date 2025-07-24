from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from models.models import User, Question, Feedback
from schemas.schemas import QuestionCreate, QuestionUpdate

router = APIRouter()

@router.get("/admin/users")
def list_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [{"id": u.id, "name": u.name, "email": u.email, "ability": u.ability} for u in users]

@router.post("/admin/questions")
def add_question(payload: QuestionCreate, db: Session = Depends(get_db)):
    question = Question(
        question=payload.question,
        choices=payload.choices,
        correct_answer=payload.correct_answer,
        difficulty=payload.difficulty
    )
    db.add(question)
    db.commit()
    db.refresh(question)
    return {"message": "Question added", "id": question.id}

@router.put("/admin/questions")
def update_question(payload: QuestionUpdate, db: Session = Depends(get_db)):
    q = db.query(Question).filter(Question.id == payload.question_id).first()
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")
    q.question = payload.question
    q.choices = payload.choices
    q.correct_answer = payload.correct_answer
    q.difficulty = payload.difficulty
    db.commit()
    return {"message": "Question updated"}

@router.delete("/admin/questions/{question_id}")
def delete_question(question_id: int, db: Session = Depends(get_db)):
    q = db.query(Question).filter(Question.id == question_id).first()
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")
    db.delete(q)
    db.commit()
    return {"message": "Question deleted"}

@router.get("/admin/analytics")
def analytics_summary(db: Session = Depends(get_db)):
    users = db.query(User).all()
    feedbacks = db.query(Feedback).all()
    responses = db.query(QuizResponse).all()

    avg_ability = sum(u.ability for u in users) / len(users) if users else 0
    avg_feedback_len = sum(len(f.content) for f in feedbacks) / len(feedbacks) if feedbacks else 0
    correct = sum(1 for r in responses if r.is_correct)
    accuracy = correct / len(responses) if responses else 0

    return {
        "total_users": len(users),
        "total_questions": db.query(Question).count(),
        "total_feedbacks": len(feedbacks),
        "avg_feedback_length": round(avg_feedback_len, 2),
        "avg_user_ability": round(avg_ability, 2),
        "overall_accuracy": round(accuracy, 2)
    }
