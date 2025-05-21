# Sample MCP-Use Project: Web Browsing Agent

This project demonstrates how to use the `mcp-use` library to create a simple web browsing agent. The agent uses an LLM (OpenAI's GPT-4o by default) and the Playwright MCP server to answer queries by browsing the web.

## How it Works

The `main.py` script initializes an `MCPClient` configured to use a Playwright MCP server. This server is defined in `browser_mcp.json` and is launched using `npx`. An `MCPAgent` is then created with an OpenAI LLM and the `MCPClient`. When the agent is run with a query (e.g., "Find the best restaurant in San Francisco USING GOOGLE SEARCH"), it leverages the Playwright server to perform web searches and browse pages to find the answer.

## Setup

1.  **Clone the repository (or download the files in this directory).**
2.  **Ensure Python 3.11+ is installed.**
3.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Set up API Keys:**
    Create a `.env` file in this directory (`sample-mcp-project/.env`) and add your OpenAI API key:
    ```
    OPENAI_API_KEY=your_openai_api_key_here
    ```
6.  **Ensure `npx` is installed.**
    `npx` is part of Node.js. If you don't have it, install Node.js (which includes npm and npx) from [https://nodejs.org/](https://nodejs.org/).
    The Playwright MCP server (`@playwright/mcp@latest`) will be downloaded and run by `npx` automatically when the script starts. Depending on your system, you might also need to ensure that the necessary Playwright browser drivers are installed or can be installed by Playwright. Often, the first run of Playwright (which `npx @playwright/mcp@latest` will trigger) handles this. You might also need to install Playwright browsers using `npx playwright install`.

## Running the Agent

Once everything is set up, run the agent:
```bash
python main.py
```

The agent will then attempt to answer the query: "Find the best restaurant in San Francisco USING GOOGLE SEARCH". You can modify this query in `main.py` to ask different questions.
