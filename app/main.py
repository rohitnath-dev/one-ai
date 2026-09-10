from app import call_ai
import os


AVAILABLE_COMMANDS = ["/help", "/clear", "/exit"]


def get_response(user_input):
    response = call_ai(user_input)
    return response


print("""
────────────────────────────────────
              ONE
────────────────────────────────────

THINK LESS. ASK MORE.

Type anything to talk to AI.
Type /help for available commands..
""")


while True:
    user_input = input("ONE › ")
    input_parts = user_input.split()

    if user_input.startswith("/"):
        command_name = input_parts[0]

        if command_name in AVAILABLE_COMMANDS:

            if command_name == "/exit":
                print("Goodbye.")
                break

            elif command_name == "/help":
                print("""
ONE COMMANDS

/help     Show available commands
/clear    Clear the terminal
/exit     Exit ONE

Type anything to talk to AI.
""")

            elif command_name == "/clear":
                os.system("clear")

        else:
            print("Unknown command. Try /help.")

    else:
        print()
        print(get_response(user_input))
        print()