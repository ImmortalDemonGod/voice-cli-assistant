import pyaudio
import time
import wave
from pathlib import Path

def test_audio_device():
    print("Testing audio input device...")
    p = pyaudio.PyAudio()
    
    try:
        # List all audio devices
        print("\nAvailable audio input devices:")
        for i in range(p.get_device_count()):
            device_info = p.get_device_info_by_index(i)
            if device_info['maxInputChannels'] > 0:
                print(f"Device {i}: {device_info['name']}")
        
        # Test recording
        print("\nRecording 3 seconds of audio for testing...")
        stream = p.open(format=pyaudio.paFloat32,
                       channels=1,
                       rate=16000,
                       input=True,
                       frames_per_buffer=1024)
        
        frames = []
        for _ in range(0, int(16000 / 1024 * 3)):
            data = stream.read(1024)
            frames.append(data)
        
        stream.stop_stream()
        stream.close()
        
        # Save test recording
        test_dir = Path("test_recordings")
        test_dir.mkdir(exist_ok=True)
        test_file = test_dir / "test_recording.wav"
        
        with wave.open(str(test_file), 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(p.get_sample_size(pyaudio.paFloat32))
            wf.setframerate(16000)
            wf.writeframes(b''.join(frames))
        
        print(f"\nTest recording saved to {test_file}")
        print("Audio device test completed successfully")
        return True
        
    except Exception as e:
        print(f"Error testing audio device: {e}")
        return False
    finally:
        p.terminate()

if __name__ == "__main__":
    test_audio_device()