
"""
This is the response that the Gradio Chat Interface uses.
Change this logic in case you want to edit how the interface works.
"""

from agents import financial_agent

def agent_response(message, history):
    messages = history + [{"role": "user", "content": message}]

    response = financial_agent.invoke(
        {"messages" : messages},
        {"configurable" : {"thread_id" : "memo_001"}}
        )

    return response["messages"][-1].content