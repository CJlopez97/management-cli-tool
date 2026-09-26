from typing import List
from models.person import Person
from models.project import Project

class User(Person):
    user_count = 0  # Class attribute counter

    def __init__(self, name: str, email: str = "", projects: List[Project] = None):
        super().__init__(name, email)
        self.projects = projects if projects is not None else []
        User.user_count += 1

    def add_project(self, project: Project):
        self.projects.append(project)

    def find_project(self, title: str):
        for proj in self.projects:
            if proj.title.lower() == title.lower():
                return proj
        return None

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "email": self.email,
            "projects": [p.to_dict() for p in self.projects]
        }

    @classmethod
    def from_dict(cls, data: dict):
        projects = [Project.from_dict(p) for p in data.get("projects", [])]
        return cls(
            name=data.get("name", ""),
            email=data.get("email", ""),
            projects=projects
        )

    def __str__(self):
        return f"User: {self.name} ({self.email}) - Projects: {len(self.projects)}"