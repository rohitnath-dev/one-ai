import os
import json
import sys
from dotenv import load_dotenv


if getattr(sys, "frozen", False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ENV_FILE = os.path.join(BASE_DIR, ".env")

load_dotenv(ENV_FILE)

SETTINGS_FILE = os.path.expanduser("~/.one/settings.json")

DEFAULT_LLM_API_KEY = os.getenv("LLM_API_KEY")
DEFAULT_LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "openrouter/free"
)
DEFAULT_LLM_BASE_URL = os.getenv(
    "LLM_BASE_URL",
    "https://openrouter.ai/api/v1/chat/completions"
)
DEFAULT_LLM_TIMEOUT = int(os.getenv("LLM_TIMEOUT", "12"))

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


def load_user_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {}

    try:
        with open(SETTINGS_FILE, "r") as file:
            data = json.load(file)

        if isinstance(data, dict):
            return data

    except (OSError, json.JSONDecodeError):
        pass

    return {}


def save_user_settings(settings):
    os.makedirs(os.path.dirname(SETTINGS_FILE), exist_ok=True)

    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)


def get_llm_config():
    user_settings = load_user_settings()

    return {
        "api_key": user_settings.get(
            "api_key",
            DEFAULT_LLM_API_KEY
        ),
        "model": user_settings.get(
            "model",
            DEFAULT_LLM_MODEL
        ),
        "base_url": user_settings.get(
            "base_url",
            DEFAULT_LLM_BASE_URL
        ),
        "timeout": DEFAULT_LLM_TIMEOUT,
    }