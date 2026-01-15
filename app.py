#  uvicorn app:app --reload

from fastapi import FastAPI
from routes.chat import router as chat_router

app = FastAPI()
app.include_router(chat_router)



@app.get("/health/")
def health_check():
    return {"status": "ok"}


