import typer
from pathlib import Path
from typing import Optional
from .audio_capture import AudioCapture
from ..processing.transcriber import Transcriber
from ..processing.analyzer import Analyzer

app = typer.Typer()
audio_capture = AudioCapture()
transcriber = Transcriber()
analyzer = Analyzer()

@app.command()
def start():
    """Start recording audio"""
    if not audio_capture.is_recording:
        audio_capture.start_recording()
        typer.echo("Recording started...")
    else:
        typer.echo("Already recording...")

@app.command()
def stop():
    """Stop recording audio"""
    if audio_capture.is_recording:
        audio_capture.stop_recording()
        recordings_dir = Path("recordings")
        recordings_dir.mkdir(exist_ok=True)
        filename = recordings_dir / "last_recording.wav"
        if audio_capture.save_recording(str(filename)):
            typer.echo(f"Recording saved to {filename}")
        else:
            typer.echo("No recording to save")
    else:
        typer.echo("Not currently recording")

@app.command()
def process():
    """Process last recording"""
    recording_file = Path("recordings/last_recording.wav")
    if not recording_file.exists():
        typer.echo("No recording found")
        return
    
    text = transcriber.transcribe(str(recording_file))
    if text:
        typer.echo(f"Transcription: {text}")
        insights = analyzer.analyze(text)
        typer.echo(f"Insights: {insights}")
    else:
        typer.echo("Failed to transcribe recording")

@app.command()
def insights():
    """Show recent insights"""
    recent_insights = analyzer.get_recent_insights()
    if recent_insights:
        for insight in recent_insights:
            typer.echo(insight)
    else:
        typer.echo("No recent insights found")