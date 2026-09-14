from app.ai import call_ai, should_search, generate_search_query
from app.web_search import search_web

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table


console = Console()


AVAILABLE_COMMANDS = {
    "/help": "Show available commands",
    "/clear": "Clear the terminal",
    "/exit": "Exit ONE",
}


def get_response(user_input):
    with console.status("[cyan]Thinking...[/cyan]", spinner="dots") as status:

        if should_search(user_input):
            status.update("[cyan]Searching the web...[/cyan]")
            search_query = generate_search_query(user_input)
            search_results = search_web(search_query)

            if search_results:
                status.update("[cyan]Generating response...[/cyan]")
                return call_ai(user_input, context=search_results)

        status.update("[cyan]Generating response...[/cyan]")
        return call_ai(user_input)


def show_intro():
    console.print(
        Panel(
            "[bold cyan]ONE[/bold cyan]\n"
            "[dim]Think less. Ask more.[/dim]\n\n"
            "Type anything to talk to AI.\n"
            "Type [bold]/help[/bold] for available commands.",
            border_style="cyan",
            padding=(1, 3),
        )
    )


def show_help():
    table = Table(
        title="[bold cyan]ONE COMMANDS[/bold cyan]",
        border_style="dim",
        show_header=True,
    )

    table.add_column("Command", style="bold cyan")
    table.add_column("Description")

    for command, description in AVAILABLE_COMMANDS.items():
        table.add_row(command, description)

    console.print(table)

    console.print(
        "\n[dim]Type anything to talk to AI.[/dim]"
    )


show_intro()


while True:
    user_input = console.input(
        "\n[bold cyan]ONE[/bold cyan] [dim]›[/dim] "
    ).strip()

    if not user_input:
        continue

    if user_input.startswith("/"):
        command = user_input.split()[0]

        if command not in AVAILABLE_COMMANDS:
            console.print(
                "[red]Unknown command.[/red] Try [bold]/help[/bold]."
            )
            continue

        if command == "/help":
            show_help()

        elif command == "/clear":
            console.clear()
            show_intro()

        elif command == "/exit":
            console.print("[dim]Goodbye.[/dim]")
            break

    else:
        response = get_response(user_input)

        console.print(
            Panel(
                Markdown(response),
                border_style="dim",
                padding=(0, 1),
            )
        )