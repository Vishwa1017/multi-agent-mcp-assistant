Personal Multi-Agent MCP Assistant

A modular AI assistant built using LangChain, LangGraph memory, MCP tools, and Streamlit.

This project demonstrates a multi-agent architecture where a router agent analyzes user questions and delegates them to specialized agents based on the domain of the query.

The assistant currently supports two domains:

Self-help and productivity books

Software engineering and system design books

The system is designed to be extensible so additional agents such as a planner agent, context summarizer, or architecture advisor can be added easily.

Overview

The assistant is built around the concept of specialized agents coordinated by a router agent.

Instead of using a single large prompt to answer every question, the router determines which domain expert should respond.

Current agents:

Self-Help Agent
Provides insights and actionable advice based on well-known self-improvement books.

Software Engineering Agent
Provides guidance on programming practices, software architecture, system design, and engineering principles.

Router Agent
Analyzes the user query and calls the appropriate specialized agent.

The system also maintains conversational state using LangGraph memory.

Model Context Protocol (MCP)

This project integrates with tools exposed through the Model Context Protocol (MCP).

MCP is a protocol designed to allow language models to interact with external tools and knowledge systems in a standardized way. Instead of embedding all knowledge directly into prompts or model weights, MCP allows models to dynamically retrieve information from external services.

In this project, MCP servers provide structured access to book knowledge and domain-specific information. The agents use MCP tools to retrieve relevant insights and return structured responses.

Benefits of MCP in this architecture include:

modular integration with external knowledge sources

separation between reasoning agents and data providers

easier extensibility when adding new tools

better maintainability compared to monolithic prompts

The MCP client connects to external tool servers and exposes those tools to LangChain agents, allowing them to query book knowledge when needed.

Features

Multi-agent architecture with domain-specific agents.

Router agent that decides which expert should handle a question.

Support for self-help and productivity knowledge.

Support for software engineering and system design knowledge.

Streamlit-based chat interface for real-time interaction.

LangGraph-based memory to maintain conversational context.

Modular design that allows additional agents to be added easily.

Architecture

The system architecture follows a layered agent design.

User
↓
Streamlit Chat Interface
↓
Router Agent
↓
Specialized Agents
↓
MCP Tools / Knowledge Sources

The router agent determines which specialized agent should respond to the query.

Each specialized agent focuses on a specific knowledge domain and retrieves information through MCP tools when necessary.

Project Structure
multi-agent-mcp
│
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── router_agent.py
│   ├── SelfHelpAgent.py
│   └── SDEAgent.py
│
├── frontend
│   └── streamlit_app.py
│
├── .streamlit
│   └── config.toml
│
├── requirements.txt
├── .gitignore
└── README.md

The app directory contains the backend agent logic.

The frontend directory contains the Streamlit chat interface.

Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/multi-agent-mcp-assistant.git
cd multi-agent-mcp-assistant

Create a virtual environment:

python -m venv venv

Activate the virtual environment.

Windows:

venv\Scripts\activate

Mac or Linux:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
Environment Variables

Create a .env file in the project root.

Example:

OPENAI_API_KEY=your_api_key_here

Additional configuration variables can be added to config.py if needed.

Running the Application

Run the Streamlit frontend from the project root:

streamlit run frontend/streamlit_app.py

After running the command, Streamlit will start a local server and provide a URL similar to:

http://localhost:8501

Open this URL in a browser to interact with the assistant.

Example Queries

Self-help related questions:

How can I build consistent habits?
Give key lessons from Atomic Habits
How do I stay productive while coding?

Software engineering related questions:

Explain clean code principles
How should I design a scalable backend?
What does Clean Code say about naming conventions?

The router agent will automatically select the appropriate specialized agent.

Future Improvements

Context manager agent for summarizing long conversations.

Planner agent for generating project or learning roadmaps.

Persistent memory instead of in-memory checkpointers.

Better agent visibility in the UI.

Support for additional MCP tools and knowledge domains.

Deployment configuration for production environments.

Technology Stack

Python
LangChain
LangGraph
Model Context Protocol (MCP)
Streamlit

Purpose of the Project

This project explores agentic AI system design and demonstrates how multiple specialized agents can collaborate to provide better answers than a single general-purpose model.

It serves as a learning project and foundation for building more advanced AI assistants.

License

MIT License