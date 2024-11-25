import json
from pathlib import Path
from typing import List, Dict
from datetime import datetime

class Storage:
    def __init__(self, storage_dir: str = "data"):
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(exist_ok=True)
        self.insights_file = self.storage_dir / "insights.json"
        self._init_storage()

    def _init_storage(self):
        if not self.insights_file.exists():
            self.insights_file.write_text("[]")

    def save_insight(self, insight: Dict):
        insights = self._load_insights()
        insight["timestamp"] = datetime.now().isoformat()
        insights.append(insight)
        self._save_insights(insights)

    def get_recent_insights(self, limit: int = 5) -> List[Dict]:
        insights = self._load_insights()
        return sorted(insights, 
                     key=lambda x: x.get("timestamp", ""), 
                     reverse=True)[:limit]

    def _load_insights(self) -> List[Dict]:
        try:
            return json.loads(self.insights_file.read_text())
        except Exception:
            return []

    def _save_insights(self, insights: List[Dict]):
        self.insights_file.write_text(json.dumps(insights, indent=2))