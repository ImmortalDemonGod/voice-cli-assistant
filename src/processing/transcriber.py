import whisper
from pathlib import Path
from typing import Optional

class Transcriber:
    def __init__(self, model_name: str = "base"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_file: str) -> Optional[str]:
        try:
            result = self.model.transcribe(audio_file)
            return result["text"]
        except Exception as e:
            print(f"Transcription error: {e}")
            return None