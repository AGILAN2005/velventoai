from sqlalchemy import Column, Integer, String, Float, DateTime
from db.database import Base
from datetime import datetime

class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, index=True)
    question = Column(String)
    answer = Column(String)
    score = Column(Float)
    feedback = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
