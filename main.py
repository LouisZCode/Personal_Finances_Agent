
from functions import read_csvs_in_folder
from agents import financial_agent
import gradio as gr



def agent_response(message, history):
    messages = history + [{"role": "user", "content": message}]

    response = financial_agent.invoke(
        {"messages" : messages},
        {"configurable" : {"thread_id" : "memo_001"}}
        )

    return response["messages"][-1].content


demo = gr.ChatInterface(
    fn=agent_response,
    title="Personal Balance Sheet Expert"
)

demo.launch()