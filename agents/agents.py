
from langchain_core.prompts import prompt
from langgraph.graph.state import Checkpoint
import yaml
import os
from langchain.agents import create_agent
from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver
from functions import read_balance_sheet

load_dotenv()

def load_prompts():
    """Load all prompts from prompts.yaml file"""
    with open("agents/prompts.yaml", "r", encoding="utf-8") as f:
        prompts = yaml.safe_load(f)
    return prompts

prompts = load_prompts()
test_prompt = prompts["test_prompt"]
financial_agent_prompt = prompts["financial_agent_prompt"]



financial_agent = create_agent(
    system_prompt=financial_agent_prompt,
    model="anthropic:claude-haiku-4-5",
    checkpointer=InMemorySaver(),
    tools=[read_balance_sheet]
)