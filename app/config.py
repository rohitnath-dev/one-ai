import os
from dotenv import load_dotenv

load_dotenv()

LLM_API_KEY = os.getenv("LLM_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

LLM_MODEL = "google/gemma-4-31b-it:free"
LLM_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"