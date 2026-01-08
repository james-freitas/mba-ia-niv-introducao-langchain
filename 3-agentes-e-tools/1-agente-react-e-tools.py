from langchain.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PrompotTemplate
from dotenv import load_dotenv

load_dotenv()

@tool("calculator", return_direct=True)
def calculator(expression: str) -> str:
    """Evaluate a simple mathematical expression and returns the result."""
    try:
        result = eval(expression)
    except Exception as e:
        return f"Error: {e}"
    return str(result)


@tool("web_search_mock")
def web_search_mock(query: str) -> str:
    """"Mocked web search tool. Returns a hardcoded result."""

    data = {"Brazil": "Brasilia", "France": "Paris", "Germany": "Berlin", "Italy": "Rome", "Spain": "Madrid"}
