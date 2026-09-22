import requests


def call_groq(
    query,
    api_key,
    model,
    base_url="https://api.groq.com/openai/v1",
    system_prompt=None,
    max_tokens=500,
    timeout=12,
):
    if not api_key:
        return "Groq API key is missing."

    url = base_url.rstrip("/")

    if not url.endswith("/chat/completions"):
        url += "/chat/completions"

    messages = []

    if system_prompt:
        messages.append({
            "role": "system",
            "content": system_prompt
        })

    messages.append({
        "role": "user",
        "content": query
    })

    try:
        response = requests.post(
            url=url,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": messages,
                "max_tokens": max_tokens,
            },
            timeout=timeout,
        )

        response.raise_for_status()

        data = response.json()

        choices = data.get("choices")

        if not choices:
            return "Groq returned no response."

        message = choices[0].get("message", {})
        content = message.get("content")

        if not content:
            return "Groq returned an empty response."

        return content.strip()

    except requests.exceptions.Timeout:
        return "Groq request timed out."

    except requests.exceptions.ConnectionError:
        return "Unable to connect to Groq."

    except requests.exceptions.HTTPError:
        try:
            error = response.json().get("error", {})
            message = error.get("message")

            if message:
                return f"Groq error: {message}"
        except Exception:
            pass

        return f"Groq returned HTTP {response.status_code}."

    except requests.exceptions.RequestException:
        return "A network error occurred while contacting Groq."

    except (ValueError, TypeError, KeyError):
        return "Groq returned an invalid response."


def call_openrouter(
    query,
    api_key,
    model,
    base_url="https://openrouter.ai/api/v1",
    system_prompt=None,
    max_tokens=500,
    timeout=12,
):
    if not api_key:
        return "OpenRouter API key is missing."

    url = base_url.rstrip("/")

    if not url.endswith("/chat/completions"):
        url += "/chat/completions"

    messages = []

    if system_prompt:
        messages.append({
            "role": "system",
            "content": system_prompt
        })

    messages.append({
        "role": "user",
        "content": query
    })

    try:
        response = requests.post(
            url=url,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": messages,
                "max_tokens": max_tokens,
            },
            timeout=timeout,
        )

        response.raise_for_status()

        data = response.json()

        choices = data.get("choices")

        if not choices:
            return "OpenRouter returned no response."

        message = choices[0].get("message", {})
        content = message.get("content")

        if not content:
            return "OpenRouter returned an empty response."

        return content.strip()

    except requests.exceptions.Timeout:
        return "OpenRouter request timed out."

    except requests.exceptions.ConnectionError:
        return "Unable to connect to OpenRouter."

    except requests.exceptions.HTTPError:
        try:
            error = response.json().get("error", {})
            message = error.get("message")

            if message:
                return f"OpenRouter error: {message}"
        except Exception:
            pass

        return f"OpenRouter returned HTTP {response.status_code}."

    except requests.exceptions.RequestException:
        return "A network error occurred while contacting OpenRouter."

    except (ValueError, TypeError, KeyError):
        return "OpenRouter returned an invalid response."