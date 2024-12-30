import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.agent import Agent, RunResponse
from phi.utils.pprint import pprint_run_response
from typing import Iterator
# Load environment variables
load_dotenv()

# Define the Agents
web_search_Agent = Agent(
    name="Websearch engine",
    role="Search the web for the information",
    model=Groq(id="llama3-groq-8b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    # show_tools_calls=True,
    markdown=True,
)

financial_agent = Agent(
    name="financial agent",
    model=Groq(id="llama3-groq-8b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            # company_news=True,
        )
    ],
    instructions=["Use tables to display the data"],
    # show_tool_calls=True,
    markdown=True,
)

multi_Ai_Agent = Agent(
    team=[web_search_Agent, financial_agent],
    instructions=["Always include sources", "Use tables to display the data"],
    model=Groq(id="llama3-groq-8b-8192-tool-use-preview"),
    # show_tool_calls=True,
    markdown=True,
)

# Streamlit UI
st.title("Financial AI Agent Dashboard")
st.sidebar.header("User Input")

# User Input
query = st.text_area("Enter your query:", )

# Button to Execute
if st.button("Submit"):

    # Call the agent
    response = multi_Ai_Agent.run(query, stream = False)

    # Display the response
    st.markdown("Answer to your query:")
    st.markdown(response.content)
