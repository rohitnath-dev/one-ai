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


DEFAULT_PROVIDER = os.getenv("DEFAULT_PROVIDER", "groq").lower()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-20b"
)

GROQ_BASE_URL = os.getenv(
    "GROQ_BASE_URL",
    "https://api.groq.com/openai/v1"
)


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

OPENROUTER_MODEL = os.getenv(
    "OPENROUTER_MODEL",
    "openrouter/free"
)

OPENROUTER_BASE_URL = os.getenv(
    "OPENROUTER_BASE_URL",
    "https://openrouter.ai/api/v1"
)


DEFAULT_LLM_TIMEOUT = int(
    os.getenv("LLM_TIMEOUT", "12")
)

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
    os.makedirs(
        os.path.dirname(SETTINGS_FILE),
        exist_ok=True
    )

    with open(SETTINGS_FILE, "w") as file:
        json.dump(
            settings,
            file,
            indent=4
        )


def get_llm_config():
    user_settings = load_user_settings()

    provider = user_settings.get(
        "provider",
        DEFAULT_PROVIDER
    ).lower()

    if provider not in ("groq", "openrouter"):
        provider = "groq"

    provider_settings = user_settings.get(
        "providers",
        {}
    ).get(
        provider,
        {}
    )

    if provider == "groq":
        return {
            "provider": "groq",
            "api_key": provider_settings.get(
                "api_key",
                GROQ_API_KEY
            ),
            "model": provider_settings.get(
                "model",
                GROQ_MODEL
            ),
            "base_url": provider_settings.get(
                "base_url",
                GROQ_BASE_URL
            ),
            "timeout": DEFAULT_LLM_TIMEOUT,
        }

    return {
        "provider": "openrouter",
        "api_key": provider_settings.get(
            "api_key",
            OPENROUTER_API_KEY
        ),
        "model": provider_settings.get(
            "model",
            OPENROUTER_MODEL
        ),
        "base_url": provider_settings.get(
            "base_url",
            OPENROUTER_BASE_URL
        ),
        "timeout": DEFAULT_LLM_TIMEOUT,
    }