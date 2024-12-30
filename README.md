# AI_FINANCIAL_AGENT
AI_AGENT
# README for Financial AI Agent Dashboard

## Overview
The **Financial AI Agent Dashboard** is a Streamlit-based application that uses advanced AI agents to provide comprehensive financial and web search solutions. This tool integrates multiple agents powered by the Groq model to deliver accurate, reliable, and structured responses to user queries.

## Features
1. **Web Search Agent**  
   - Searches the web for information using DuckDuckGo.  
   - Always includes sources for credibility.  
   - Powered by the `Groq` model.  

2. **Financial Agent**  
   - Retrieves financial data using YFinance tools, such as stock prices, analyst recommendations, and stock fundamentals.  
   - Displays data in tables for better readability.  

3. **Multi-Agent Collaboration**  
   - Combines the Web Search Agent and Financial Agent to provide enriched responses.  
   - Ensures structured data presentation and source inclusion.  

4. **Streamlit UI**  
   - Simple and user-friendly interface.  
   - Allows users to input queries and view detailed, markdown-formatted responses.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/financial-ai-agent-dashboard.git
   cd financial-ai-agent-dashboard
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:  
   Create a `.env` file and add the necessary environment variables required for the agents.

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Launch the application using the command above.  
2. Enter your query in the text area provided on the main page.  
3. Click the **Submit** button to get results.  
4. View the response, including tables and sources, directly in the UI.

## Dependencies
- [Streamlit](https://streamlit.io/)  
- [Phi Library](https://example.com)  
- [Python Dotenv](https://pypi.org/project/python-dotenv/)  
- [YFinanceTools](https://pypi.org/project/yfinance/)  
- [DuckDuckGo API](https://api.duckduckgo.com/)

## Customization
- Modify the agents in `app.py` to add or change tools and instructions.
- Update the `Groq` model IDs to use other compatible models if needed.
- Customize the UI using Streamlit components.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for bugs, feature requests, or improvements.

