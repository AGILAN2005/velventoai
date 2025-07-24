from fastapi import FastAPI
from routes.user_routes import user_router
from routes.learn_routes import learn_router
from routes import feedback
from db.database import Base,engine
app = FastAPI()
app.include_router(user_router)
app.include_router(learn_router)
app.include_router(feedback.router)
Base.metadata.create_all(bind=engine)
