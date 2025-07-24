from fastapi import FastAPI
from routes import quiz, feedback
from db.database import Base, engine
from routes import gamification,llm_questions,roadmap
app = FastAPI()

# Base.metadata.drop_all(bind=engine) 
Base.metadata.create_all(bind=engine)

app.include_router(quiz.router)
app.include_router(feedback.router)
app.include_router(roadmap.router)
app.include_router(gamification.router)
app.include_router(llm_questions.router)

