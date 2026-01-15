from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from agents import financial_agent


router = APIRouter()

class ChatBody(BaseModel):
    message : str

@router.post("/chat/")
async def agent_response(request : ChatBody):
    try:
        messages = [{"role": "user", "content": request.message}]

        response = await financial_agent.ainvoke(
            {"messages" : messages},
            {"configurable" : {"thread_id" : "memo_001"}}
            )

        return response["messages"][-1].content
    except Exception as e:
        HTTPException(status_code=500, detail=f"agent error: {str(e)}")