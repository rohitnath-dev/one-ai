from rich.console import Console
from rich.panel import Panel

from config import (
    DEFAULT_LLM_API_KEY,
    DEFAULT_LLM_MODEL,
    DEFAULT_LLM_BASE_URL,
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


def show_current_settings():
    settings = load_user_settings()

    api_key = settings.get("api_key", DEFAULT_LLM_API_KEY)
    model = settings.get("model", DEFAULT_LLM_MODEL)
    base_url = settings.get("base_url", DEFAULT_LLM_BASE_URL)

    console.print(
        Panel(
            f"[bold]Model:[/bold] {model}\n"
            f"[bold]Provider:[/bold] {base_url}\n"
            f"[bold]API Key:[/bold] {mask_key(api_key)}",
            title="ONE Settings",
            border_style="cyan",
        )
    )


def change_api_key():
    settings = load_user_settings()

    console.print("\n[dim]Enter your API key.[/dim]")
    console.print("[dim]Leave empty to keep the current key.[/dim]")

    api_key = console.input("API Key: ").strip()

    if not api_key:
        return

    settings["api_key"] = api_key
    save_user_settings(settings)

    console.print("[green]API key updated.[/green]")


def change_model():
    settings = load_user_settings()

    console.print("\n[dim]Example: google/gemma-4-31b-it:free[/dim]")

    model = console.input("Model: ").strip()

    if not model:
        return

    settings["model"] = model
    save_user_settings(settings)

    console.print("[green]Model updated.[/green]")


def change_provider():
    settings = load_user_settings()

    console.print("\n[dim]Enter the provider's OpenAI-compatible Chat Completions URL.[/dim]")
    console.print(
        "[dim]Example: https://openrouter.ai/api/v1/chat/completions[/dim]"
    )

    base_url = console.input("Base URL: ").strip()

    if not base_url:
        return

    settings["base_url"] = base_url
    save_user_settings(settings)

    console.print("[green]Provider updated.[/green]")


def reset_settings():
    settings = load_user_settings()

    settings.pop("api_key", None)
    settings.pop("model", None)
    settings.pop("base_url", None)

    save_user_settings(settings)

    console.print("[green]Settings reset to defaults.[/green]")


def open_settings():
    while True:
        console.print("\n[bold cyan]ONE SETTINGS[/bold cyan]")
        console.print("1. Change API key")
        console.print("2. Change model")
        console.print("3. Change provider")
        console.print("4. Show current settings")
        console.print("5. Reset to defaults")
        console.print("6. Back")

        choice = console.input("\nSelect: ").strip()

        if choice == "1":
            change_api_key()

        elif choice == "2":
            change_model()

        elif choice == "3":
            change_provider()

        elif choice == "4":
            show_current_settings()

        elif choice == "5":
            reset_settings()

        elif choice == "6":
            break

        else:
            console.print("[red]Invalid option.[/red]")