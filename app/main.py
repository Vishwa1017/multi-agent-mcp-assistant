import asyncio
from json import tool
import string
from urllib import response
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.tools import tool

from SelfHelpAgent import build_books_agent
from SDEAgent import build_sde_agent
from config import THREAD_ID


async def main():


    @tool
    async def self_help_agent(query: str) -> str:
        """
            Use this tool when the user asks about:
            - productivity
            - habits
            - mindset
            - self-improvement
            - discipline
            - motivation
            - focus
            - advice from self-help books

            Books covered include:
            Atomic Habits, Make Time, Think Straight, Just Do It, Mindset.
            """
        agent = await build_books_agent()
        response = await agent.ainvoke(
        {"messages": [HumanMessage(content=query)]},
        config,
    )
        return response["messages"][-1].content
    

    @tool
    async def sde_agent(query: str) -> str:
        """
    Use this tool when the user asks about:
    - software engineering
    - programming practices
    - clean code
    - system design
    - design patterns
    - refactoring
    - algorithms
    - building software systems

    Books covered include:
    Clean Code, Pragmatic Programmer, Designing Data-Intensive Applications,
    System Design Interview, Head First Design Patterns, Refactoring,
    Grokking Algorithms, Code Complete.
    """
        agent = await build_sde_agent()
        response = await agent.ainvoke(
        {"messages": [HumanMessage(content=query)]},
        config,
    )
        return response["messages"][-1].content

    query = input("Ask something: ")

    config = {"configurable": {"thread_id": THREAD_ID}}

    main_agent = create_agent(
    model='gpt-5-nano',
    tools=[self_help_agent, sde_agent],
    system_prompt="""
You are a routing assistant.

You MUST use the available tools to answer questions.

Available tools:

1. self_help_agent
Use this when the question is about:
- habits
- productivity
- mindset
- self improvement
- motivation
- books like Atomic Habits, Make Time, Mindset

2. sde_agent
Use this when the question is about:
- software engineering
- clean code
- design patterns
- system design
- algorithms
- programming practices
- books like Clean Code, Pragmatic Programmer, Refactoring

If the question relates to either domain, DO NOT answer yourself.
Always call the correct tool.
""")
    response = await main_agent.ainvoke(
        {"messages": [HumanMessage(content=query)]},
        config,
    )
    print("\nAssistant:\n")
    print(response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())