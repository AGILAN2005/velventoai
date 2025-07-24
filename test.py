import requests
import random

BASE_URL = "http://localhost:8000"

def register_user():
    res = requests.post(f"{BASE_URL}/register_user", json={
        "username": "testuser1",
        "email": "testuser1@example.com"
    })
    print("✅ Register User:", res.json())
    return res.json().get("user_id")

def generate_questions(topic="Time Complexity"):
    res = requests.post(f"{BASE_URL}/generate-questions/", json={"topic": topic})
    print("✅ Generate Questions:", res.status_code)
    return res.json()

def get_next_question(user_id):
    res = requests.get(f"{BASE_URL}/next_question", params={"user_id": user_id})
    print("✅ Next Question:", res.json())
    return res.json()

def submit_answer(user_id, question_id, options, correct_answer):
    chosen = random.choice(options)
    res = requests.post(f"{BASE_URL}/submit_answer", json={
        "user_id": user_id,
        "question_id": question_id,
        "selected_option": chosen,
        "is_correct": (chosen == correct_answer)
    })
    print("✅ Submit Answer:", res.json())

def submit_feedback(user_id, question_id):
    res = requests.post(f"{BASE_URL}/submit-feedback", json={
        "user_id": user_id,
        "question_id": question_id,
        "difficulty_rating": random.choice(["easy", "medium", "hard"]),
        "feedback_text": "Good question"
    })
    print("✅ Submit Feedback:", res.json())

def update_gamification(user_id):
    res = requests.post(f"{BASE_URL}/gamification/update", json={
        "user_id": user_id,
        "points_earned": random.randint(1, 10),
        "badge_earned": "Quick Thinker"
    })
    print("✅ Update Gamification:", res.json())

def get_gamification_status(user_id):
    res = requests.get(f"{BASE_URL}/gamification/status/{user_id}")
    print("✅ Gamification Status:", res.json())

# ---- TEST SEQUENCE ----

user_id = register_user()
questions = generate_questions()

if questions:
    for q in questions:
        question_id = q.get("id") or q.get("question_id", 1)  # adjust as needed
        options = q.get("options", [])
        answer = q.get("answer", options[0] if options else None)

        if question_id and options and answer:
            submit_answer(user_id, question_id, options, answer)
            submit_feedback(user_id, question_id)
            update_gamification(user_id)

# Fetch current progress
get_next_question(user_id)
get_gamification_status(user_id)
