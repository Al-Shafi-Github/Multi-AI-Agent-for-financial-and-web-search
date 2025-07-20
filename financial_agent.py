import phi
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")
import phi

##web search agent
web_search_agent = Agent(
    name= "web search Agent",
    role= "Search the web for information",
    model= Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include Sources"],
    show_tool_calls=True,
    markdown=True,
)

## Financial Agent

finance_agent= Agent(
    name="Finance AI Agent",
    model= Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent= Agent(
    team=[web_search_agent, finance_agent],
    model= Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    instructions=["Always include Sources", "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recomendation and share the lattest news for NVDA", stream=True)