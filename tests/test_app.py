# import requests

# BASE = "http://127.0.0.1:8000"

# # Register a user
# user = requests.post(f"{BASE}/register_user", json={"name": "Test User"}).json()
# uid = user["user_id"]

# # Get a question
# question = requests.get(f"{BASE}/next_question", params={"user_id": uid}).json()
# print("QUESTION:", question)

# # Submit answer
# answer = requests.post(f"{BASE}/submit_answer", json={
#     "user_id": uid,
#     "question_id": question["question_id"],
#     "user_answer": "42"
# }).json()
# print("ANSWER RESULT:", answer)

# # Submit feedback
# feedback = requests.post(f"{BASE}/submit-feedback", json={
#     "user_id": uid,
#     "comment": "I enjoyed the adaptive questions, but they could be more challenging."
# }).json()
# print("SUMMARY:", feedback)









from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    ability = Column(Float, default=0.0)

class QuizResponse(Base):
    __tablename__ = "quiz_responses"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer)
    is_correct = Column(Boolean)

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    question = Column(String)
    choices = Column(String)  # You may use JSON column type depending on your DB
    correct_answer = Column(String)
    difficulty = Column(Float)

class Feedback(Base):
    __tablename__ = "feedbacks"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String)
