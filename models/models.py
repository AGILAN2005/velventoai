from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSON,TEXT  # ✅ Required for JSON column
from db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ability = Column(Float, default=0.0)
    gamification = relationship("Gamification", back_populates="user", uselist=False)

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String)
    level = Column(String)
    content = Column(TEXT)
    correct_answer = Column(String)
    options = Column(JSON)  # ✅ Native PostgreSQL JSON field
    user_id = Column(Integer, ForeignKey("users.id"))

    
class Answer(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    user_answer = Column(String)
    is_correct = Column(Boolean)

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    comment = Column(String)

class Summary(Base):
    __tablename__ = "summary"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    summary_text = Column(String)

class QuizResponse(Base):
    __tablename__ = "quiz_responses"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer)
    is_correct = Column(Boolean)

class Gamification(Base):
    __tablename__ = "gamification"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    xp = Column(Integer, default=0)
    level = Column(Integer, default=1)
    badges = Column(String, default="")  # CSV of badge names

    user = relationship("User", back_populates="gamification")
