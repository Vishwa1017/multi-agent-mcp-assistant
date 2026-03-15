from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

from app.config import BOOKS_MCP_URL, MODEL_NAME, BOOK_LIST


async def build_books_agent():
    client = MultiServerMCPClient(
        {
            "books_server": {
                "transport": "streamable_http",
                "url": BOOKS_MCP_URL,
            }
        }
    )

    tools = await client.get_tools()

    books_text = ", ".join(BOOK_LIST)

    system_prompt = f"""
You are a helpful book assistant.

Focus mainly on these books:
{books_text}

Give practical, concise, useful takeaways.
If relevant, combine ideas across these books.
"""

    agent = create_agent(
        MODEL_NAME,
        tools=tools,
        checkpointer=InMemorySaver(),
        system_prompt=system_prompt,
    )

    return agent