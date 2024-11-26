import pyaudio
import wave
from pathlib import Path

def test_audio_device():
    """Test audio input by recording a short sample."""
    print("Testing audio input device...")
    p = pyaudio.PyAudio()
    
    try:
        # Get default input device info
        default_device_index = p.get_default_input_device_info()['index']
        default_device_name = p.get_device_info_by_index(default_device_index)['name']
        print(f"\nUsing default audio input device: {default_device_name} (Index: {default_device_index})")
        
        print("\nRecording 3 seconds of audio for testing...")
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
        for _ in range(0, int(sample_rate / chunk * 3)):
            data = stream.read(chunk, exception_on_overflow=False)
            frames.append(data)
        
        # Stop and close the stream
        stream.stop_stream()
        stream.close()

        # Save the test recording
        test_dir = Path("test_recordings")
        test_dir.mkdir(exist_ok=True)
        test_file = test_dir / "test_recording.wav"
        
        with wave.open(str(test_file), 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(format_type))
            wf.setframerate(sample_rate)
            wf.writeframes(b''.join(frames))
        
        print(f"\nTest recording saved to {test_file}")
        print("Audio device test completed successfully.")
        return True

    except Exception as e:
        print(f"Error testing audio device: {e}")
        return False

    finally:
        p.terminate()


if __name__ == "__main__":
    test_audio_device()