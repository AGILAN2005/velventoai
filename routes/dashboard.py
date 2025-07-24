from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from models.models import User, QuizResponse, Feedback
from schemas.schemas import DashboardResponse

router = APIRouter()

@router.get("/dashboard/{user_id}", response_model=DashboardResponse)
def get_user_dashboard(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": "User not found"}
    
    responses = db.query(QuizResponse).filter(QuizResponse.user_id == user_id).all()
    feedbacks = db.query(Feedback).filter(Feedback.user_id == user_id).all()

    if not responses:
        accuracy = 0.0
    else:
        correct = sum(1 for r in responses if r.is_correct)
        accuracy = correct / len(responses)

    ability = user.ability
    feedback_summary = " / ".join([f.content for f in feedbacks[-3:]])

    return {
        "user_id": user.id,
        "ability": ability,
        "accuracy": round(accuracy, 2),
        "feedback_summary": feedback_summary or "No feedback yet"
    }

@router.get("/dashboard/summary")
def get_system_summary(db: Session = Depends(get_db)):
    users = db.query(User).all()
    total_users = len(users)
    avg_ability = sum(u.ability for u in users) / total_users if total_users else 0.0

    all_responses = db.query(QuizResponse).all()
    if not all_responses:
        overall_accuracy = 0.0
    else:
        correct = sum(1 for r in all_responses if r.is_correct)
        overall_accuracy = correct / len(all_responses)

    top_users = sorted(users, key=lambda x: x.ability, reverse=True)[:5]
    top_summary = [{"id": u.id, "name": u.name, "ability": u.ability} for u in top_users]

    return {
        "total_users": total_users,
        "average_ability": round(avg_ability, 2),
        "overall_accuracy": round(overall_accuracy, 2),
        "top_performers": top_summary
    }
