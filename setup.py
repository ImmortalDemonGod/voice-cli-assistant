from setuptools import setup, find_packages

setup(
    name="voice_cli_assistant",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "typer",
        "pyaudio",
        "openai-whisper",
        "numpy",
        "fastapi",
        "python-multipart",
        "pyyaml"
    ],
    entry_points={
        "console_scripts": [
            "voice-cli=core.cli:app",
        ],
    },
    python_requires=">=3.11",
)