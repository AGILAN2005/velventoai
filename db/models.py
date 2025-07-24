from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, index=True)
    subject = Column(String, nullable=False)
    score = Column(Float, nullable=False)
    comments = Column(String, nullable=False)
