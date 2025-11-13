import random
import sys
from rich.console import Console
from pitsoferrors.data import victory_quotes, easter_eggs
from pitsoferrors.core import build_unique_insults

console = Console()

CORRECT = 7
TOTAL = 50
ATTEMPTS = 0

def main():
    console.print("[bold cyan]Welcome to PitsofErrors[/bold cyan]")
    console.print(f"Find the correct number between 1 and {TOTAL}. The abyss awaits.\n")

    insult_pool = build_unique_insults()
    used_insults = set()
    previous_number = None
    global ATTEMPTS

    while True:
        try:
            user_input = input("Enter your number: ").strip()

            if user_input.lower() == "help":
                console.print("[bold yellow]Help? There is none here.[/bold yellow]")
                continue

            if not user_input.isdigit():
                console.print("[bold red]That’s not even a number.[/bold red]")
                continue

            num = int(user_input)
            ATTEMPTS += 1

            if num == CORRECT:
                console.print(f"[bold green]{random.choice(victory_quotes)}[/bold green]")
                console.print(f"[italic]Attempts: {ATTEMPTS}[/italic]")
                break

            if num in easter_eggs:
                console.print(f"[bold magenta]{easter_eggs[num]}[/bold magenta]")
            else:
                if insult_pool:
                    insult = insult_pool.pop()
                    used_insults.add(insult)
                    console.print(f"[bold red]Error![/bold red] {insult}")
                else:
                    fallback = f"Even after {ATTEMPTS} attempts, your brain remains an unhandled exception."
                    console.print(f"[bold red]{fallback}[/bold red]")

            previous_number = num

        except KeyboardInterrupt:
            console.print("\n[bold red]Escaping the pit already? Figures.[/bold red]")
            sys.exit(0)
