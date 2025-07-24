import math
from sqlalchemy.orm import Session
from models.models import User, Question
from sqlalchemy import func

def probability_correct(theta, b):
    return 1 / (1 + math.exp(-(theta - b)))

def update_ability(theta, b, correct, lr=0.1):
    p = probability_correct(theta, b)
    error = correct - p
    return theta + lr * error

def select_adaptive_question(db: Session, user: User):
    return db.query(Question).order_by(func.abs(Question.difficulty - user.ability)).first()
