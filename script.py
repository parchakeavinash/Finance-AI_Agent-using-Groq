from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os

# Using the same Groq model that worked in your test
groq_model = Groq(
    id="llama3-70b-8192",  # Using the more powerful 70b model for better analysis
    api_key=os.environ.get("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")
)

# web search agent
web_search_agent = Agent(
    name="Web search agent",
    role="search",
    model=groq_model,
    tool=[DuckDuckGo()],
    instructions=['Always include sources'],
    show_tools_calls=True,
    markdown=True
)

# financial search agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=groq_model,
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

# Multi-agent setup
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    instructions=['Always include sources', 'use table to display the data'],
    show_tool_calls=True,
    markdown=True
)

# Test the agent
multi_ai_agent.print_response("summarize analyst recommendation and share the latest news for Apple", stream=True)