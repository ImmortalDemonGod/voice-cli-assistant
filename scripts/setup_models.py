import whisper
import os
from pathlib import Path

def setup_models():
    print("Downloading Whisper base model...")
    try:
        # This will download the model if it's not already cached
        model = whisper.load_model("base")
        print("Model downloaded successfully")
        return True
    except Exception as e:
        print(f"Error downloading model: {e}")
        return False

if __name__ == "__main__":
    setup_models()