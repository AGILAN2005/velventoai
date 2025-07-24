from fastapi import APIRouter
from db.user_db import get_user, update_user
from utils.feedback import generate_prompt
from utils.irt import update_irt_score
from utils.gemini_api import call_gemini

learn_router = APIRouter()

@learn_router.get("/next_question")
def next_question(user: str):
    user_data = get_user(user)
    prompt = generate_prompt(user_data)
    question = call_gemini(prompt)
    return {"question": question}

@learn_router.post("/submit_answer")
def submit_answer(user: str, question: str, user_answer: str, correct_answer: str):
    user_data = get_user(user)
    correct = user_answer.strip().lower() == correct_answer.strip().lower()
    new_score = update_irt_score(user_data["irt_score"], correct)
    user_data["irt_score"] = new_score
    user_data["history"].append({
        "question": question,
        "user_answer": user_answer,
        "correct_answer": correct_answer,
        "correct": correct
    })
    update_user(user, user_data)
    return {
        "correct": correct,
        "new_score": new_score
    }
