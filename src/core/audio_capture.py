import pyaudio
import wave
import numpy as np
from typing import Optional

class AudioCapture:
    def __init__(self, channels: int = 1, rate: int = 16000, chunk: int = 1024):
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.format = pyaudio.paFloat32
        self.audio = pyaudio.PyAudio()
        self.stream: Optional[pyaudio.Stream] = None
        self.frames = []
        self.is_recording = False

    def start_recording(self):
        self.stream = self.audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk
        )
        self.frames = []
        self.is_recording = True

    def stop_recording(self):
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None
        self.is_recording = False

    def save_recording(self, filename: str):
        if not self.frames:
            return False
        
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.audio.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(self.frames))
        return True

    def __del__(self):
        if self.stream:
            self.stream.close()
        self.audio.terminate()