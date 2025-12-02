
"""
Creation of the demo UI ChatInterface for LLM conversation.
Launches in main.py
"""

import gradio as gr
from functions import agent_response

demo = gr.ChatInterface(
    fn=agent_response,
    title="Personal Balance Sheet Expert"
)