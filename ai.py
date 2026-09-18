import requests
import json
import time

from prompts import SYSTEM_PROMPT, SEARCH_DECISION_PROMPT, SEARCH_QUERY_PROMPT
from config import get_llm_config


def call_ai(query, system_prompt=SYSTEM_PROMPT, context=None, max_tokens=500):

    config = get_llm_config()

    llm_api_key = config["api_key"]
    llm_model = config["model"]
    llm_base_url = config["base_url"]
    llm_timeout = config["timeout"]

    if not llm_api_key:
        return "API key is missing. Add your API key in settings."

    user_content = query

    if context:
        user_content = f"""
User query:
{query}

Web search results:
{context}

Answer the user's original query using the search results when relevant.
"""

    max_retries = 2

    for attempt in range(max_retries):
        try:
            response = requests.post(
                url=llm_base_url,
                headers={
                    "Authorization": f"Bearer {llm_api_key}",
                    "Content-Type": "application/json"
                },
                data=json.dumps({
                    "model": llm_model,
                    "messages": [
                        {
                            "role": "system",
                            "content": system_prompt
                        },
                        {
                            "role": "user",
                            "content": user_content
                        }
                    ],
                    "max_tokens": max_tokens
                }),
                timeout=llm_timeout
            )

        except requests.exceptions.Timeout:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue

            return "The request timed out. Please try again."

        except requests.exceptions.ConnectionError:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue

            return "Unable to connect to the AI provider."

        except requests.exceptions.RequestException:
            return "A network error occurred. Please try again."

        try:
            data = response.json()

        except json.JSONDecodeError:
            if response.status_code >= 500 and attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue

            return "The AI provider returned an invalid response."

        status_code = response.status_code

        if status_code in (429, 502, 503, 504):
            if attempt < max_retries - 1:
                retry_after = response.headers.get("Retry-After")

                try:
                    wait_time = float(retry_after)

                except (TypeError, ValueError):
                    wait_time = 2 ** attempt

                time.sleep(min(wait_time, 10))
                continue

            if status_code == 429:
                return "The AI provider is temporarily rate-limited. Please try again shortly."

            return "The AI provider is temporarily unavailable. Please try again."

        if status_code == 401:
            return "Invalid API key."

        if status_code == 402:
            return "The API provider requires available credits for this request."

        if status_code == 400:
            return "The AI request was invalid."

        if status_code == 403:
            return "The AI provider rejected this request."

        if status_code != 200:
            error_message = None

            if isinstance(data, dict):
                error = data.get("error")

                if isinstance(error, dict):
                    error_message = error.get("message")

            if error_message:
                return f"AI provider error: {error_message}"

            return f"AI provider returned HTTP {status_code}."

        if not isinstance(data, dict):
            return "The AI provider returned an unexpected response."

        choices = data.get("choices")

        if not isinstance(choices, list) or not choices:
            return "The AI provider returned no response."

        message = choices[0].get("message")

        if not isinstance(message, dict):
            return "The AI provider returned an invalid message."

        answer = message.get("content")

        if not isinstance(answer, str) or not answer.strip():
            return "I couldn't generate a response."

        return answer.strip()

    return "Unable to get a response from the AI provider."


def should_search(query):
    for attempt in range(2):
        decision = call_ai(
            query,
            system_prompt=SEARCH_DECISION_PROMPT,
            max_tokens=5
        )

        decision = decision.strip().upper()

        if decision == "TRUE":
            return True

        if decision == "FALSE":
            return False

    return False


def generate_search_query(query):
    search_query = call_ai(
        query,
        system_prompt=SEARCH_QUERY_PROMPT,
        max_tokens=50
    )

    return search_query.strip()