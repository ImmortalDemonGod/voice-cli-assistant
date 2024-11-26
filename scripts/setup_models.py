import whisper
import os
from pathlib import Path

def setup_models(model_name="base"):
    """
    Downloads and caches the specified Whisper model.
    
    Parameters:
        model_name (str): Name of the Whisper model to download (default: "base").
        
    Returns:
        bool: True if the model was downloaded successfully, False otherwise.
    """
    print(f"Downloading Whisper '{model_name}' model...")
    try:
        # Check if the model is already cached by loading it
        model = whisper.load_model(model_name)
        print(f"Model '{model_name}' downloaded and cached successfully.")
        return True
    except Exception as e:
        print(f"Error downloading model '{model_name}': {e}")
        return False

if __name__ == "__main__":
    # Set the default model name to "base"
    model_name = "base"
    
    # Check if a custom model name was provided via environment variables
    custom_model_name = os.getenv("WHISPER_MODEL_NAME")
    if custom_model_name:
        print(f"Custom model name detected: {custom_model_name}")
        model_name = custom_model_name

    # Call the setup_models function
    success = setup_models(model_name)
    if success:
        print("Model setup complete.")
    else:
        print("Model setup failed. Please check the error logs.")