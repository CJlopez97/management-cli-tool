from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def print_success(message: str):
    console.print(f"[bold green]✓[/bold green] {message}")

def print_error(message: str):
    console.print(f"[bold red]✗ Error:[/bold red] {message}")

def print_projects_table(user_name: str, projects: list):
    table = Table(title=f"Projects for {user_name}")
    table.add_column("Title", style="cyan", no_wrap=True)
    table.add_column("Description", style="white")
    table.add_column("Due Date", style="magenta")
    table.add_column("Total Tasks", style="yellow")

    for proj in projects:
        table.add_row(proj.title, proj.description, proj.due_date, str(len(proj.tasks)))

    console.print(table)

def print_summary_panel(project_title: str, summary_text: str):
    console.print(Panel(summary_text, title=f"AI Summary: {project_title}", border_style="blue"))