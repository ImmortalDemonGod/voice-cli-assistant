from typing import List, Optional
from .storage import Storage

class Analyzer:
    def __init__(self):
        self.storage = Storage()

    def analyze(self, text: str) -> Optional[dict]:
        # Placeholder for LLM analysis pipeline
        # Will be implemented with actual LLM integration
        if text:
            insight = {"text": text, "type": "raw_transcription"}
            self.storage.save_insight(insight)
            return insight
        return None

    def get_recent_insights(self, limit: int = 5) -> List[dict]:
        return self.storage.get_recent_insights(limit)