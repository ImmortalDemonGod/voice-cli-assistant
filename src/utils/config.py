import yaml
from pathlib import Path
from typing import Dict, Any

class Config:
    def __init__(self, config_file: str = "config/default_config.yml"):
        self.config_file = Path(config_file)
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        if not self.config_file.exists():
            return self._create_default_config()
        
        with open(self.config_file, 'r') as f:
            return yaml.safe_load(f)

    def _create_default_config(self) -> Dict[str, Any]:
        default_config = {
            'audio': {
                'channels': 1,
                'rate': 16000,
                'chunk': 1024
            },
            'voice_control': {
                'wake_word': 'assistant',
                'threshold': 0.5
            },
            'transcriber': {
                'model': 'base'
            }
        }
        
        self.config_file.parent.mkdir(exist_ok=True)
        with open(self.config_file, 'w') as f:
            yaml.dump(default_config, f)
        
        return default_config

    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        return value if value is not None else default