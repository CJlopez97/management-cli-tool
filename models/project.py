from typing import List
from models.task import Task

class Project:
    def __init__(self, title: str, description: str = "", due_date: str = "N/A", tasks: List[Task] = None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = tasks if tasks is not None else []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def find_task(self, title: str):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                return task
        return None

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [t.to_dict() for t in self.tasks]
        }

    @classmethod
    def from_dict(cls, data: dict):
        tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
        return cls(
            title=data.get("title", ""),
            description=data.get("description", ""),
            due_date=data.get("due_date", "N/A"),
            tasks=tasks
        )

    def __repr__(self):
        return f"<Project: {self.title} ({len(self.tasks)} tasks)>"