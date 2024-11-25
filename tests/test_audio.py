import pytest
from src.core.audio_capture import AudioCapture
import os

def test_audio_capture_init():
    capture = AudioCapture()
    assert capture.channels == 1
    assert capture.rate == 16000
    assert capture.chunk == 1024
    assert not capture.is_recording

def test_recording_state():
    capture = AudioCapture()
    capture.start_recording()
    assert capture.is_recording
    capture.stop_recording()
    assert not capture.is_recording

def test_save_recording(tmp_path):
    capture = AudioCapture()
    filename = str(tmp_path / "test.wav")
    
    # Test with no frames
    assert not capture.save_recording(filename)
    assert not os.path.exists(filename)