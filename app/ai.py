import requests
import json
from app import SYSTEM_PROMPT
from app.config import LLM_API_KEY

def call_ai(query):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",

        headers={
            "Authorization": f"Bearer {LLM_API_KEY}",
            "Content-Type": "application/json"
        },

        data=json.dumps({
            "model": "~openai/gpt-latest",
            "messages": [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": query
                }
            ],
            "max_tokens": 32
        })
    )

    data = response.json()

    if response.status_code != 200:
        return data["error"]["message"]
    else:
        answer = data["choices"][0]["message"]["content"]

    return answer