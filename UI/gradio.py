
"""
Creation of the demo UI ChatInterface for LLM conversation.
Launches in main.py
"""

# UI/gradio.py
import gradio as gr
import requests

def agent_response(message, history):
    response = requests.post(
        "http://127.0.0.1:8000/chat/",
        json={"message": message}
    )
    return response.json()

demo = gr.ChatInterface(
    fn=agent_response,
    title="Personal Balance Sheet Expert"
)