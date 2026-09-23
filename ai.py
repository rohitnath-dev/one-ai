from prompts import SYSTEM_PROMPT, SEARCH_DECISION_PROMPT, SEARCH_QUERY_PROMPT
from config import get_llm_config
from providers import call_groq, call_openrouter


def call_ai(query, system_prompt=SYSTEM_PROMPT, context=None, max_tokens=500):

    config = get_llm_config()

    provider = config["provider"]

    user_content = query

    if context:
        user_content = f"""
User query:
{query}

Web search results:
{context}

Answer the user's original query using the search results when relevant.
"""

    if provider == "openrouter":
        return call_openrouter(
            user_content,
            config["api_key"],
            config["model"],
            config["base_url"],
            system_prompt,
            max_tokens,
            config["timeout"]
        )

    elif provider == "groq":
        return call_groq(
            user_content,
            config["api_key"],
            config["model"],
            config["base_url"],
            system_prompt,
            max_tokens,
            config["timeout"]
        )

    else:
        return "Please enter a valid provider (groq or openrouter)"


def should_search(query):
    decision = call_ai(
        query,
        system_prompt=SEARCH_DECISION_PROMPT,
        max_tokens=50
    )

    decision = decision.strip().upper().rstrip(".")

    return decision == "TRUE"


def generate_search_query(query):
    search_query = call_ai(
        query,
        system_prompt=SEARCH_QUERY_PROMPT,
        max_tokens=50
    )

    return search_query.strip()