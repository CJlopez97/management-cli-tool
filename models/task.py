class Task:
    def __init__(
        self,
        title: str,
        status: str = "Pending",
        assigned_to: str = "Unassigned"
    ):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str):
        allowed_statuses = ["Pending", "In Progress", "Completed"]

        if value not in allowed_statuses:
            raise ValueError(
                "Status must be Pending, In Progress, or Completed."
            )

        self._status = value

    def mark_complete(self):
        self.status = "Completed"

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            title=data.get("title", ""),
            status=data.get("status", "Pending"),
            assigned_to=data.get("assigned_to", "Unassigned")
        )

    def __repr__(self):
        return f"<Task: {self.title} [{self.status}]>"