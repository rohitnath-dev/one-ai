import requests
from config import TAVILY_API_KEY


def search_web(query):
    if not TAVILY_API_KEY:
        return None

    try:
        response = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": TAVILY_API_KEY,
                "query": query,
                "max_results": 5,
            },
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()
        results = data.get("results", [])

        if not results:
            return None

        formatted_results = []

        for result in results:
            formatted_results.append(
                f"Title: {result.get('title', '')}\n"
                f"Content: {result.get('content', '')}\n"
                f"URL: {result.get('url', '')}"
            )

        return "\n\n".join(formatted_results)

    except requests.RequestException:
        return None
