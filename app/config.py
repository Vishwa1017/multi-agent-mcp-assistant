import os
from dotenv import load_dotenv

load_dotenv()

BOOKS_MCP_URL = os.getenv(
    "BOOKS_MCP_URL",
    "https://classic-books-mcp.chensong8804.workers.dev/mcp"
)

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-5-nano")
THREAD_ID = os.getenv("THREAD_ID", "1")

SELF_HELP_BOOKS = [
    "Make Time",
    "Think Straight",
    "Just Do It",
    "Atomic Habits",
    "Mindset",
]

SDE_BOOKS = [
    "Clean Code",
    "The Pragmatic Programmer",
    "Designing Data-Intensive Applications",
    "System Design Interview",
    "Head First Design Patterns",
    "Refactoring",
    "Grokking Algorithms",
    "Code Complete"
]