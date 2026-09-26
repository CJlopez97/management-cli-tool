import os
import json
from typing import List
from models.user import User

class StorageService:
    def __init__(self, file_path: str = "data/project_data.json"):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            self.save_users([])

    def load_users(self) -> List[User]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [User.from_dict(u) for u in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_users(self, users: List[User]):
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump([u.to_dict() for u in users], f, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")