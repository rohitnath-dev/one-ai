from tavily import Client
from app.config import TAVILY_API_KEY


tavily_client = Client(api_key=TAVILY_API_KEY)


def search_web(query):
    if not TAVILY_API_KEY:
        return None

    try:
        response = tavily_client.search(
            query=query,
            max_results=5
        )

        results = response.get("results", [])

        if not results:
            return None

        formatted_results = []

        for result in results:
            title = result.get("title", "")
            content = result.get("content", "")
            url = result.get("url", "")

            formatted_results.append(
                f"Title: {title}\n"
                f"Content: {content}\n"
                f"URL: {url}"
            )

        return "\n\n".join(formatted_results)

    except Exception:
        return None