from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.openai import OpenAIChat
import openai

import os
from dotenv import load_dotenv 
openai.api_key = os.getenv("OPENAI_API_KEY")

# web search agent
web_search_agent = Agent(
    name="Web search agent",
    role="search",
    model=OpenAIChat(id="gpt-3.5-turbo"),  # Changed model name
    tool=[DuckDuckGo()],
    instructions=['Always include sources'],
    show_tools_calls=True,
    markdown=True
)

# financial search agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=OpenAIChat(id="gpt-3.5-turbo"), 
    tool=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
        ),
    ],
    instructions=['use table to display the data'],
    show_tools_calls=True,
    markdown=True
)

multi_ai_agent = Agent(
    team=[web_search_agent,finance_agent],
    instructions=['Alway include sources','use table to display the data'],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response("summarize analyst recommendation and share  the latest news for Apple",stream=True)