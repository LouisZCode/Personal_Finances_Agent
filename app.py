#  uvicorn app:app --reload

from fastapi import FastAPI
from pydantic import BaseModel
from agents import financial_agent


app = FastAPI()

class ChatBody(BaseModel):
    message : str

@app.get("/health/")
def health_check():
    return {"status": "ok"}

@app.post("/chat/")
async def agent_response(request : ChatBody):
    messages = [{"role": "user", "content": request.message}]

    response = await financial_agent.ainvoke(
        {"messages" : messages},
        {"configurable" : {"thread_id" : "memo_001"}}
        )

    return response["messages"][-1].content