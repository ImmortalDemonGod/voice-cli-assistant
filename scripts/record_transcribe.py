import whisper
import pyaudio
import wave
from pathlib import Path

def setup_models(model_name="base"):
    """
    Downloads and caches the specified Whisper model.
    """
    print(f"Downloading Whisper '{model_name}' model...")
    try:
        model = whisper.load_model(model_name)
        print(f"Model '{model_name}' downloaded and cached successfully.")
        return model
    except Exception as e:
        print(f"Error downloading model '{model_name}': {e}")
        return None

def test_audio_device():
    """
    Test audio input by recording a short sample.
    """
    print("Testing audio input device...")
    p = pyaudio.PyAudio()
    try:
        # Get default input device info
        default_device_index = p.get_default_input_device_info()['index']
        default_device_name = p.get_device_info_by_index(default_device_index)['name']
        print(f"Using default audio input device: {default_device_name} (Index: {default_device_index})")
        
        print("Recording 5 seconds of audio...")
        sample_rate = 44100  # High-quality audio
        format_type = pyaudio.paInt16  # Standard format for WAV compatibility
        channels = 1
        chunk = 1024

        # Open the audio stream
        stream = p.open(format=format_type,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk,
                        input_device_index=default_device_index)
        
        frames = []
        for _ in range(0, int(sample_rate / chunk * 5)):
            data = stream.read(chunk, exception_on_overflow=False)
            frames.append(data)
        
        # Stop and close the stream
        stream.stop_stream()
        stream.close()

        # Save the recording
        recordings_dir = Path("recordings")
        recordings_dir.mkdir(exist_ok=True)
        audio_file = recordings_dir / "recorded_audio.wav"
        
        with wave.open(str(audio_file), 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(format_type))
            wf.setframerate(sample_rate)
            wf.writeframes(b''.join(frames))
        
        print(f"Audio recording saved to {audio_file}")
        return audio_file

    except Exception as e:
        print(f"Error testing audio device: {e}")
        return None

    finally:
        p.terminate()

def transcribe_audio(model, audio_file):
    """
    Transcribe the given audio file using Whisper.
    """
    try:
        print(f"Transcribing audio file: {audio_file}")
        result = model.transcribe(str(audio_file))
        print("\nTranscription:")
        print(result["text"])
        return result["text"]
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

if __name__ == "__main__":
    # Step 1: Setup Whisper model
    model = setup_models("base")
    if model is None:
        print("Failed to load Whisper model. Exiting...")
        exit(1)

    # Step 2: Test audio input and record a sample
    audio_file = test_audio_device()
    if audio_file is None:
        print("Failed to record audio. Exiting...")
        exit(1)

    # Step 3: Transcribe the recorded audio
    transcribed_text = transcribe_audio(model, audio_file)
    if transcribed_text is not None:
        print("\nTranscription completed successfully.")