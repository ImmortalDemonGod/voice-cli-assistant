# Voice CLI Assistant

Personal voice-controlled CLI system for note-taking and decision support.

## Features
- Voice-activated command system
- Real-time audio transcription
- Task and insight extraction
- Mobile recording support (planned)

## Setup
1. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or .\venv\Scripts\activate on Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run setup script:
   ```bash
   python scripts/setup_models.py
   ```

## Usage
Basic commands:
```bash
voice-cli start    # Start recording
voice-cli stop     # Stop recording
voice-cli process  # Process last recording
voice-cli insights # Show recent insights
```

## Development Status
Currently implementing Phase 1: Core CLI & Voice Control