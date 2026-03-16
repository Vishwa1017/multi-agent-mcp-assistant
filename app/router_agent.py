from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.tools import tool

from .SelfHelpAgent import build_books_agent
from .SDEAgent import build_sde_agent


ROUTER_PROMPT = """
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
- discipline
- focus
- books like Atomic Habits, Make Time, Mindset, Think Straight

2. sde_agent
Use this when the question is about:
- software engineering
- clean code
- design patterns
- system design
- algorithms
- programming practices
- architecture
- books like Clean Code, Pragmatic Programmer, Refactoring, DDIA

If the question relates to either domain, DO NOT answer yourself.
Always call the correct tool.
"""


async def build_router_agent(thread_id: str):
    config = {"configurable": {"thread_id": thread_id}}

    books_agent = await build_books_agent()
    software_agent = await build_sde_agent()

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
        response = await books_agent.ainvoke(
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
        Clean Code, The Pragmatic Programmer, Designing Data-Intensive Applications,
        System Design Interview, Head First Design Patterns, Refactoring,
        Grokking Algorithms, Code Complete.
        """
        response = await software_agent.ainvoke(
            {"messages": [HumanMessage(content=query)]},
            config,
        )
        return response["messages"][-1].content

    main_agent = create_agent(
        model="gpt-5-nano",
        tools=[self_help_agent, sde_agent],
        system_prompt=ROUTER_PROMPT,
    )

    return main_agent


async def ask_router_agent(main_agent, thread_id: str, user_message: str) -> str:
    config = {"configurable": {"thread_id": thread_id}}

    response = await main_agent.ainvoke(
        {"messages": [HumanMessage(content=user_message)]},
        config,
    )

    return response["messages"][-1].content