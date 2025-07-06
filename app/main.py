from fastapi import FastAPI
from app.routes.chat import router as chat_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Healthcare Chatbot",
    description="A chatbot for answering healthcare questions",
    version="0.0.1",
)

app.include_router(chat_router, prefix="/chat")


@app.get("/")
async def root():
    return {"message": "Welcome to our Healthcare Chatbot!"}
