import os
import dotenv
from mem0 import MemoryClient
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown
from rich import box

dotenv.load_dotenv()
MEM0_API_KEY = os.getenv("MEM0_KEY")
USER_ID = "neoscribe"

client = MemoryClient(api_key=MEM0_API_KEY)
console = Console()

def display_memories(results):
    if not results:
        console.print("[bold red]⚠ No memories found.[/bold red]")
        return

    for idx, item in enumerate(results, 1):
        role = item.get("role", "user").capitalize()
        content = item.get("memory", "No content available")

        console.print(Panel.fit(
            Markdown(content),
            title=f"[bold cyan]{role}[/bold cyan] Entry #{idx}",
            border_style="magenta",
            box=box.ROUNDED,
            padding=(1, 2),
        ))

def search_loop():
    console.print("[bold magenta]🔍 Welcome to NeoScribe Memory Viewer[/bold magenta]")
    console.print("Type a topic or keyword to search your stored flashcards, notes, or quizzes.")
    console.print("[grey70]Type 'exit' to quit.[/grey70]\n")

    while True:
        query = Prompt.ask("🔎 Enter your search query")
        if query.lower() in ["exit", "quit", "q"]:
            console.print("\n[bold green]👋 Exiting NeoScribe Memory Viewer.[/bold green]")
            break

        try:
            results = client.search(query=query, user_id=USER_ID, limit=10)
            display_memories(results)
        except Exception as e:
            console.print(f"[red]❌ Error searching memory:[/red] {e}")

if __name__ == "__main__":
    search_loop()
