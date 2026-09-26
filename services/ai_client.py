class AIProjectSummarizer:
    def __init__(self, model: str = "llama3"):
        self.model = model

    def summarize(self, project_data: dict) -> str:
        prompt = (
            f"Analyze this project and provide a 2-sentence summary and next step suggestion.\n"
            f"Title: {project_data.get('title')}\n"
            f"Description: {project_data.get('description')}\n"
            f"Tasks: {project_data.get('tasks')}"
        )
        try:
            import ollama
            response = ollama.chat(
                model=self.model,
                messages=[{'role': 'user', 'content': prompt}]
            )
            return response['message']['content']
        except Exception:
            # Graceful fallback when Ollama service or model is unavailable
            return self._fallback_summary(project_data)

    def _fallback_summary(self, project_data: dict) -> str:
        total_tasks = len(project_data.get("tasks", []))
        completed = sum(1 for t in project_data.get("tasks", []) if t.get("status") == "Completed")
        pending = total_tasks - completed

        return (
            f"[Offline AI Mode] Project '{project_data.get('title')}' is currently active. "
            f"It has {completed}/{total_tasks} tasks completed ({pending} pending). "
            f"Suggested Next Step: Review pending tasks and assign remaining work."
        )