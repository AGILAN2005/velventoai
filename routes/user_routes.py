from fastapi import APIRouter
from db.user_db import register_user

user_router = APIRouter()

@user_router.post("/register_user")
def register(username: str, topic: str):
    register_user(username, topic)
    return {"msg": "User registered"}
