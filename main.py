import asyncio
from langchain.messages import HumanMessage

from app.agent import build_books_agent
from app.config import THREAD_ID


async def main():
    agent = await build_books_agent()

    query = input("Ask something: ")

    config = {"configurable": {"thread_id": THREAD_ID}}

    response = await agent.ainvoke(
        {"messages": [HumanMessage(content=query)]},
        config,
    )

    print("\nAssistant:\n")
    print(response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())