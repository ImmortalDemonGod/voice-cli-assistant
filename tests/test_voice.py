import pytest
import numpy as np
from src.core.voice_control import VoiceControl

def test_voice_control_init():
    control = VoiceControl()
    assert control.wake_word == "assistant"
    assert control.threshold == 0.5
    assert not control.is_listening

def test_listening_state():
    control = VoiceControl()
    def dummy_callback(audio): pass
    
    control.start_listening(dummy_callback)
    assert control.is_listening
    assert control.command_callback is not None
    
    control.stop_listening()
    assert not control.is_listening
    assert control.command_callback is None

def test_process_audio_frame():
    control = VoiceControl()
    frame = np.zeros(1024, dtype=np.float32)
    result = control.process_audio_frame(frame)
    assert isinstance(result, bool)