import os
from dotenv import load_dotenv

load_dotenv()

BOOKS_MCP_URL = os.getenv(
    "BOOKS_MCP_URL",
    "https://classic-books-mcp.chensong8804.workers.dev/mcp"
)

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-5-nano")
THREAD_ID = os.getenv("THREAD_ID", "1")

BOOK_LIST = [
    "Make Time",
    "Think Straight",
    "Just Do It",
    "Atomic Habits",
    "Mindset",
]