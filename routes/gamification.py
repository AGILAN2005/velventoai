from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from models.models import Gamification

router = APIRouter()

def assign_badges(xp: int) -> str:
    badges = []
    if xp >= 100: badges.append("🎯 Beginner")
    if xp >= 300: badges.append("🚀 Intermediate")
    if xp >= 600: badges.append("🏆 Expert")
    return ",".join(badges)

@router.post("/gamification/update")
def update_gamification(user_id: int, xp_gain: int, db: Session = Depends(get_db)):
    gamify = db.query(Gamification).filter_by(user_id=user_id).first()
    if not gamify:
        gamify = Gamification(user_id=user_id)
        db.add(gamify)
    gamify.xp += xp_gain
    gamify.level = (gamify.xp // 100) + 1
    gamify.badges = assign_badges(gamify.xp)
    db.commit()
    return {
        "message": "Gamification updated",
        "xp": gamify.xp,
        "level": gamify.level,
        "badges": gamify.badges.split(",")
    }

@router.get("/gamification/status/{user_id}")
def get_gamification_status(user_id: int, db: Session = Depends(get_db)):
    gamify = db.query(Gamification).filter_by(user_id=user_id).first()
    if not gamify:
        return {"xp": 0, "level": 1, "badges": []}
    return {
        "xp": gamify.xp,
        "level": gamify.level,
        "badges": gamify.badges.split(",") if gamify.badges else []
    }
