import argparse
from services.storage_service import StorageService
from services.ai_client import AIProjectSummarizer
from models.user import User
from models.project import Project
from models.task import Task
from utils.formatters import print_success, print_error, print_projects_table, print_summary_panel

def main():
    storage = StorageService()
    users = storage.load_users()

    def find_user(name: str):
        for u in users:
            if u.name.lower() == name.lower():
                return u
        return None

    parser = argparse.ArgumentParser(description="CLI Project Management Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # add-user
    parser_user = subparsers.add_parser("add-user", help="Add a new user")
    parser_user.add_argument("--name", required=True, help="User name")
    parser_user.add_argument("--email", default="", help="User email")

    # list-user
    parser_user = subparsers.add_parser("list-users", help="List all users")

    # add-project
    parser_proj = subparsers.add_parser("add-project", help="Add a project to a user")
    parser_proj.add_argument("--user", required=True, help="User name")
    parser_proj.add_argument("--title", required=True, help="Project title")
    parser_proj.add_argument("--description", default="", help="Project description")
    parser_proj.add_argument("--due", default="N/A", help="Due date")

    # add-task
    parser_task = subparsers.add_parser("add-task", help="Add a task to a project")
    parser_task.add_argument("--project", required=True, help="Project title")
    parser_task.add_argument("--title", required=True, help="Task title")
    parser_task.add_argument("--assigned", default="Unassigned", help="Assigned user")

    # complete-task
    parser_comp = subparsers.add_parser("complete-task", help="Mark a task complete")
    parser_comp.add_argument("--project", required=True, help="Project title")
    parser_comp.add_argument("--task", required=True, help="Task title")

    # list-projects
    parser_list = subparsers.add_parser("list-projects", help="List user projects")
    parser_list.add_argument("--user", required=True, help="User name")

    #list-tasks
    parser_tasks = subparsers.add_parser("list-tasks", help="List all tasks for a project")
    parser_tasks.add_argument("--project", required=True, help="Project title")

    # summarize-project
    parser_sum = subparsers.add_parser("summarize-project", help="Generate AI summary for a project")
    parser_sum.add_argument("--project", required=True, help="Project title")

    args = parser.parse_args()

    if args.command == "add-user":
        if find_user(args.name):
            print_error(f"User '{args.name}' already exists.")
            return
        new_user = User(name=args.name, email=args.email)
        users.append(new_user)
        storage.save_users(users)
        print_success(f"Added user '{new_user.name}'.")

    elif args.command == "list-users":
        if not users:
         print_error("No users found.")
         return

        for user in users:
            print(user)

    elif args.command == "add-project":
        user = find_user(args.user)
        if not user:
            print_error(f"User '{args.user}' not found.")
            return
        if user.find_project(args.title):
            print_error(f"Project '{args.title}' already exists for this user.")
            return
        project = Project(title=args.title, description=args.description, due_date=args.due)
        user.add_project(project)
        storage.save_users(users)
        print_success(f"Added project '{project.title}' to user '{user.name}'.")

    elif args.command == "add-task":
        target_project = None
        for u in users:
            proj = u.find_project(args.project)
            if proj:
                target_project = proj
                break
        if not target_project:
            print_error(f"Project '{args.project}' not found.")
            return
        task = Task(title=args.title, assigned_to=args.assigned)
        target_project.add_task(task)
        storage.save_users(users)
        print_success(f"Added task '{task.title}' to project '{target_project.title}'.")

    elif args.command == "complete-task":
        target_task = None
        for u in users:
            proj = u.find_project(args.project)
            if proj:
                target_task = proj.find_task(args.task)
                break
        if not target_task:
            print_error(f"Task '{args.task}' or Project '{args.project}' not found.")
            return
        target_task.mark_complete()
        storage.save_users(users)
        print_success(f"Task '{target_task.title}' marked as completed.")

    elif args.command == "list-projects":
        user = find_user(args.user)
        if not user:
            print_error(f"User '{args.user}' not found.")
            return
        print_projects_table(user.name, user.projects)

    elif args.command == "list-tasks":
        target_project = None

        for u in users:
            proj = u.find_project(args.project)
            if proj:
                target_project = proj
                break

        if not target_project:
            print_error(f"Project '{args.project}' not found.")
            return

        if not target_project.tasks:
            print_error(f"Project '{target_project.title}' has no tasks.")
            return

        print(f"\nTasks for '{target_project.title}':")

        for task in target_project.tasks:
            print(
                f"- {task.title} | "
                f"Status: {task.status} | "
                f"Assigned to: {task.assigned_to}"
        )

    elif args.command == "summarize-project":
        target_project = None
        for u in users:
            proj = u.find_project(args.project)
            if proj:
                target_project = proj
                break
        if not target_project:
            print_error(f"Project '{args.project}' not found.")
            return
        
        summarizer = AIProjectSummarizer()
        summary = summarizer.summarize(target_project.to_dict())
        print_summary_panel(target_project.title, summary)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()