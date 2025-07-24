from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from models.models import User, Answer, Question
from schemas.schemas import UserCreate, QuestionResponse, AnswerSubmit
from utils.irt_engine import select_adaptive_question, update_ability

router = APIRouter()

@router.post("/register_user")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    user_db = User(name=user.name)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return {"user_id": user_db.id}

@router.get("/next_question", response_model=QuestionResponse)
def get_question(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    question = select_adaptive_question(db, user)
    return {"question_id": question.id, "question": question.content}

@router.post("/submit_answer")
def submit_answer(ans: AnswerSubmit, db: Session = Depends(get_db)):
    user = db.query(User).get(ans.user_id)
    question = db.query(Question).get(ans.question_id)
    is_correct = ans.user_answer.strip().lower() == question.correct_answer.strip().lower()
    
    # Save answer
    db_answer = Answer(user_id=user.id, question_id=question.id, user_answer=ans.user_answer, is_correct=is_correct)
    db.add(db_answer)

    # Update ability
    user.ability = update_ability(user.ability, question.difficulty, int(is_correct))
    db.commit()
    return {"correct": is_correct, "updated_ability": user.ability}
