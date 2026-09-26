# Project Management CLI Tool

A Python command-line project management application that allows admins to manage users, projects, and tasks. The application uses object-oriented programming, JSON persistence, `argparse` for the CLI, `Rich` for formatted output, and Ollama for AI-powered project summaries.

## Features

* Create and manage users
* Create projects for users
* Add tasks to projects
* Assign tasks to users
* Mark tasks as completed
* View projects
* View tasks
* Store data in a JSON file
* Generate AI-powered project summaries
* Provide an offline fallback when the AI service is unavailable
* Use object-oriented programming with inheritance and encapsulation
* Use formatted terminal output with Rich

## Project Structure

```text
project-management-cli/
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── user.py
│   ├── project.py
│   └── task.py
│
├── services/
│   ├── __init__.py
│   ├── storage_service.py
│   └── ai_client.py
│
├── data/
│   └── project_data.json
│
├── utils/
│   ├── __init__.py
│   └── formatters.py
│
├── requirements.txt
└── README.md
```

## Object-Oriented Design

The application uses several classes to organize the project management system.

### Person

`Person` is the parent class for users.

It demonstrates encapsulation using properties and setters for the user's name and email.

### User

`User` inherits from `Person`.

A user can have multiple projects.

```text
User
└── Projects
    ├── Project
    └── Project
```

### Project

A project contains project information such as:

* Title
* Description
* Due date
* Tasks

Each project can contain multiple tasks.

### Task

A task contains:

* Title
* Status
* Assigned user

Tasks can also be marked as completed.

### Relationships

The application uses the following relationships:

```text
User
  │
  ├── Project
  │     ├── Task
  │     └── Task
  │
  └── Project
        └── Task
```

## Requirements

* Python 3
* `pip`
* Ollama for the AI project summary feature

## Installation

Clone the repository:

```bash
git clone git@github.com:CJlopez97/management-cli-tool.git
```

Move into the project directory:

```bash
cd project-management-cli
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment on Linux/macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Ollama Setup

The project uses Ollama for AI-generated project summaries.

Install Ollama and make sure it is running.

Then download the model used by the application:

```bash
ollama pull llama3
```

You can verify that the model is available with:

```bash
ollama list
```

If Ollama is unavailable, the application uses an offline fallback summary instead of crashing.

## Running the Application

Run the application with:

```bash
python main.py
```

You can also see the available commands with:

```bash
python main.py --help
```

## CLI Commands

### Add a User

```bash
python main.py add-user --name "Alex" --email "alex@example.com"
```

### List Users

```bash
python main.py list-users
```

### Add a Project

```bash
python main.py add-project \
    --user "Alex" \
    --title "CLI Tool" \
    --description "Build a project management CLI" \
    --due "2026-10-15"
```

### List Projects

```bash
python main.py list-projects --user "Alex"
```

### Add a Task

```bash
python main.py add-task \
    --project "CLI Tool" \
    --title "Implement add-task" \
    --assigned "Alex"
```

### List Tasks

```bash
python main.py list-tasks --project "CLI Tool"
```

### Complete a Task

```bash
python main.py complete-task \
    --project "CLI Tool" \
    --task "Implement add-task"
```

### Generate an AI Project Summary

```bash
python main.py summarize-project --project "CLI Tool"
```

The AI summary provides a short description of the project's current state and suggests a possible next step.

## Data Persistence

Project information is stored in:

```text
data/project_data.json
```

The application automatically loads saved users, projects, and tasks when it starts.

Changes made through the CLI are saved back to the JSON file.

The storage service also handles missing or malformed JSON files so that the application does not crash unexpectedly.

## External Package

The project uses the following Python packages:

### Rich

Rich is used to create formatted terminal output, including tables, panels, and colored success/error messages.

The dependency is listed in:

```text
requirements.txt
```

Install all dependencies with:

```bash
pip install -r requirements.txt
```

## AI Integration

The AI functionality is separated from the CLI into:

```text
services/ai_client.py
```

The `AIProjectSummarizer` class receives structured project information and sends it to the Ollama AI service.

The service returns:

* A project summary
* A suggested next step

If the Ollama service or model is unavailable, the application uses a fallback summary based on the project's task information.

This keeps the AI service logic separate from the CLI and allows the AI implementation to be changed later without rewriting the command-line interface.

## Error Handling

The application handles several common errors, including:

* Attempting to create a duplicate user
* Attempting to create a duplicate project
* Searching for a user that does not exist
* Searching for a project that does not exist
* Searching for a task that does not exist
* Projects without tasks
* Missing JSON data
* Malformed JSON data
* AI service failures

Errors are displayed as readable messages in the terminal.

## Example Workflow

A typical workflow might look like this:

```bash
python main.py add-user --name "Alex" --email "alex@example.com"

python main.py add-project \
    --user "Alex" \
    --title "CLI Tool" \
    --description "Build a project management CLI" \
    --due "2026-10-15"

python main.py add-task \
    --project "CLI Tool" \
    --title "Implement add-task" \
    --assigned "Alex"

python main.py add-task \
    --project "CLI Tool" \
    --title "Write README" \
    --assigned "Alex"

python main.py list-projects --user "Alex"

python main.py list-tasks --project "CLI Tool"

python main.py complete-task \
    --project "CLI Tool" \
    --task "Implement add-task"

python main.py summarize-project --project "CLI Tool"
```

## Technologies Used

* Python
* Object-Oriented Programming
* `argparse`
* JSON
* Rich
* Ollama
* Git/GitHub

## OOP Concepts Demonstrated

This project demonstrates:

* Classes and objects
* Inheritance
* Encapsulation
* Properties
* Setter methods
* Class attributes
* Instance methods
* Class methods
* Object relationships
* `__str__`
* `__repr__`

## Git Workflow

Development was organized using Git feature branches and meaningful commits.

Example:

```bash
git checkout -b feature/project-management-cli

git add .
git commit -m "Add project management models"

git add .
git commit -m "Add JSON persistence"

git add .
git commit -m "Add CLI commands"

git add .
git commit -m "Add AI project summary"

git add .
git commit -m "Add project documentation"
```

The feature branch can then be pushed to GitHub and submitted through a pull request.

## Future Improvements

Possible future improvements include:

* Delete users, projects, and tasks
* Update task information from the CLI
* Search for projects and tasks
* Allow projects with duplicate titles for different users
* Add user IDs and project IDs
* Add more AI-generated project recommendations
* Add automated tests
* Add due-date validation
* Add task priority levels
* Add task filtering and sorting

## Author

Created as a Python summative project demonstrating object-oriented programming, file I/O, CLI development, external package usage, and external AI service integration.
