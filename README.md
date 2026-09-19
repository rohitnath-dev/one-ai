# ONE

> A minimal AI that won't yap.

ONE is a lightweight command-line AI assistant focused on keeping interactions simple, concise, and practical.

It can answer normally, decide when a question needs web search, retrieve relevant web information, and use that context to generate a response.

## Features

- AI-powered command-line interface
- Automatic web search when needed
- Configurable AI provider
- Configurable AI model
- Configurable API key
- Persistent local settings
- Minimal terminal interface
- Standalone Windows executable
- Pipeline tests
- No Python installation required for the Windows release

---

## Download

### Windows

<a href="https://github.com/rohitnath-dev/one-ai/releases/latest/download/ONE.exe">
  <img src="https://img.shields.io/badge/Download-ONE.exe-2ea44f?style=for-the-badge" alt="Download ONE.exe">
</a>

Download the latest Windows executable and run `ONE.exe`.

No Python installation is required for the standalone Windows release.

> **Note:** ONE requires a working AI provider/API configuration to generate responses.

---

## How ONE Works

ONE uses a simple pipeline to decide whether web search is necessary.

```
User Query
    │
    ▼
Should Search?
   /     \
 No       Yes
 │          │
 ▼          ▼
AI      Generate Search Query
            │
            ▼
        Web Search
            │
            ▼
       Search Results
            │
            ▼
       AI + Context
            │
            ▼
         Response
```

For normal queries, ONE can directly send the request to the configured AI provider.

For queries that require external or current information, ONE can perform a web search first and provide the retrieved context to the AI.

---

## Commands

| Command | Description |
|---|---|
| `/help` | Show available commands |
| `/settings` | Manage AI provider, model and API key |
| `/clear` | Clear the terminal |
| `/exit` | Exit ONE |

---

## Settings

ONE supports local configuration for:

- AI API key
- AI model
- AI provider / OpenAI-compatible endpoint

User-specific settings are stored locally at:

```
~/.one/settings.json
```

The `/settings` command can be used to change supported configuration values without modifying the source code.

---

## Web Search

ONE can determine whether a query requires web search.

When search is required, the process is:

```
User Query
    ↓
Search Decision
    ↓
Search Query Generation
    ↓
Web Search
    ↓
Search Results
    ↓
AI Response
```

Tavily is currently used as the web search provider.

If web search is unavailable, ONE can still attempt to answer the query normally through the configured AI provider.

---

## Project Structure

```
one-ai/
├── README.md
├── ai.py
├── config.py
├── main.py
├── prompts.py
├── settings.py
├── web_search.py
├── requirements.txt
└── tests/
    └── test_pipeline.py
```

Python cache files such as `__pycache__` are generated locally and are not part of the project's source structure.

### Main files

| File | Purpose |
|---|---|
| `main.py` | CLI entry point and command handling |
| `ai.py` | AI requests and search-decision pipeline |
| `config.py` | Configuration and persistent settings handling |
| `settings.py` | `/settings` interface |
| `prompts.py` | System and pipeline prompts |
| `web_search.py` | Web-search integration |
| `tests/test_pipeline.py` | Pipeline tests |
| `requirements.txt` | Python dependencies |

---

## Running From Source

### Requirements

- Python 3.13
- Internet connection
- API key for a supported AI provider
- Tavily API key if web search is required

### Installation

```bash
git clone https://github.com/rohitnath-dev/one-ai.git
cd one-ai
pip install -r requirements.txt
```

Then run:

```bash
python main.py
```

---

## Configuration

For source-code usage, configuration can be provided through environment variables.

Create a `.env` file based on `.env.example`.

Example:

```env
LLM_API_KEY=your_api_key
LLM_MODEL=your_model
LLM_BASE_URL=your_provider_endpoint
LLM_TIMEOUT=12

TAVILY_API_KEY=your_tavily_api_key
```

---

## Security

- Never commit real API keys or other secrets to the repository.
- The Windows release is built as a standalone executable. API credentials bundled into a distributed executable should not be considered secret, because an executable distributed to another person can potentially be inspected.
- For public production deployments, credentials should be kept on a server-side system rather than embedded in a client application.

---

## Testing

The project includes pipeline tests under:

```
tests/test_pipeline.py
```

Tests can be run with Python's test runner, depending on the current test implementation.

---

## Windows Release

ONE is distributed for Windows as a standalone executable.

The Windows executable is built through GitHub Actions and packaged using PyInstaller.

The current release is:

```
v1.0.0
```

See the latest release for the available release assets.

---

## Current Status

ONE is currently an early release.

**Available**
- CLI interface
- AI responses
- Automatic search decision
- Web search integration
- Configurable model/provider/API key
- Persistent settings
- Windows executable
- Basic pipeline tests

---

## Future Improvements

The project may evolve with additional features, improvements to reliability, and a more refined user experience.

---

## Contributing

ONE is open source.

If you find a bug, have an improvement, or want to contribute, feel free to open an issue or pull request.

Before contributing, please keep changes focused and consistent with the project's goal of keeping ONE simple.

---

## License

ONE is released under the MIT License.

See [LICENSE](LICENSE) for the full license text.

---

## Author

Created by **Rohit Nath**.

---

<p align="center"><i>ONE — Think less. Ask more.</i></p>
