from rich.console import Console
from rich.panel import Panel

from config import (
    DEFAULT_PROVIDER,
    GROQ_API_KEY,
    GROQ_MODEL,
    GROQ_BASE_URL,
    OPENROUTER_API_KEY,
    OPENROUTER_MODEL,
    OPENROUTER_BASE_URL,
    load_user_settings,
    save_user_settings,
)


console = Console()


def mask_key(key):
    if not key:
        return "Not set"

    if len(key) <= 8:
        return "*" * len(key)

    return key[:4] + "*" * (len(key) - 8) + key[-4:]


def get_current_provider(settings):
    provider = settings.get("provider", DEFAULT_PROVIDER)

    if provider not in ("groq", "openrouter"):
        provider = DEFAULT_PROVIDER

    return provider


def get_provider_config(provider, settings):
    providers = settings.get("providers", {})
    provider_settings = providers.get(provider, {})

    if provider == "groq":
        return {
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
        }

    return {
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
    }


def show_current_settings():
    settings = load_user_settings()

    provider = get_current_provider(settings)
    config = get_provider_config(provider, settings)

    console.print(
        Panel(
            f"[bold]Provider:[/bold] {provider}\n"
            f"[bold]Model:[/bold] {config['model']}\n"
            f"[bold]Base URL:[/bold] {config['base_url']}\n"
            f"[bold]API Key:[/bold] {mask_key(config['api_key'])}",
            title="ONE Settings",
            border_style="cyan",
        )
    )


def change_provider():
    settings = load_user_settings()

    console.print("\n[bold]Select provider:[/bold]")
    console.print("1. Groq")
    console.print("2. OpenRouter")

    choice = console.input("\nSelect: ").strip()

    if choice == "1":
        settings["provider"] = "groq"

    elif choice == "2":
        settings["provider"] = "openrouter"

    else:
        console.print("[red]Invalid provider.[/red]")
        return

    save_user_settings(settings)

    console.print(
        f"[green]Provider changed to {settings['provider']}.[/green]"
    )


def change_api_key():
    settings = load_user_settings()

    provider = get_current_provider(settings)

    console.print(
        f"\n[dim]Enter your {provider} API key.[/dim]"
    )
    console.print(
        "[dim]Leave empty to keep the current key.[/dim]"
    )

    api_key = console.input("API Key: ").strip()

    if not api_key:
        return

    providers = settings.setdefault("providers", {})

    provider_settings = providers.setdefault(
        provider,
        {}
    )

    provider_settings["api_key"] = api_key

    save_user_settings(settings)

    console.print(
        f"[green]{provider} API key updated.[/green]"
    )


def change_model():
    settings = load_user_settings()

    provider = get_current_provider(settings)
    current_config = get_provider_config(provider, settings)

    console.print(
        f"\n[dim]Current model: {current_config['model']}[/dim]"
    )

    model = console.input("Model: ").strip()

    if not model:
        return

    providers = settings.setdefault("providers", {})

    provider_settings = providers.setdefault(
        provider,
        {}
    )

    provider_settings["model"] = model

    save_user_settings(settings)

    console.print(
        f"[green]{provider} model updated.[/green]"
    )


def change_base_url():
    settings = load_user_settings()

    provider = get_current_provider(settings)
    current_config = get_provider_config(provider, settings)

    console.print(
        f"\n[dim]Current URL: {current_config['base_url']}[/dim]"
    )

    base_url = console.input("Base URL: ").strip()

    if not base_url:
        return

    providers = settings.setdefault("providers", {})

    provider_settings = providers.setdefault(
        provider,
        {}
    )

    provider_settings["base_url"] = base_url

    save_user_settings(settings)

    console.print(
        f"[green]{provider} base URL updated.[/green]"
    )


def reset_settings():
    settings = load_user_settings()

    settings.pop("provider", None)
    settings.pop("providers", None)

    save_user_settings(settings)

    console.print(
        "[green]Settings reset to defaults.[/green]"
    )


def open_settings():
    while True:
        console.print("\n[bold cyan]ONE SETTINGS[/bold cyan]")
        console.print("1. Switch provider")
        console.print("2. Change API key")
        console.print("3. Change model")
        console.print("4. Change base URL")
        console.print("5. Show current settings")
        console.print("6. Reset to defaults")
        console.print("7. Back")

        choice = console.input("\nSelect: ").strip()

        if choice == "1":
            change_provider()

        elif choice == "2":
            change_api_key()

        elif choice == "3":
            change_model()

        elif choice == "4":
            change_base_url()

        elif choice == "5":
            show_current_settings()

        elif choice == "6":
            reset_settings()

        elif choice == "7":
            break

        else:
            console.print("[red]Invalid option.[/red]")