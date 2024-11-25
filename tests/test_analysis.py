import pytest
from src.processing.analyzer import Analyzer
from src.processing.storage import Storage
from pathlib import Path
import shutil

@pytest.fixture
def analyzer():
    # Setup test storage
    test_storage_dir = Path("test_data")
    if test_storage_dir.exists():
        shutil.rmtree(test_storage_dir)
    test_storage_dir.mkdir()
    
    analyzer = Analyzer()
    analyzer.storage = Storage(str(test_storage_dir))
    yield analyzer
    
    # Cleanup
    shutil.rmtree(test_storage_dir)

def test_analyzer_init(analyzer):
    assert isinstance(analyzer, Analyzer)
    assert isinstance(analyzer.storage, Storage)

def test_analyze_text(analyzer):
    text = "Test transcription"
    result = analyzer.analyze(text)
    assert result is not None
    assert result["text"] == text
    assert result["type"] == "raw_transcription"

def test_get_recent_insights(analyzer):
    # Add some test insights
    texts = ["Test 1", "Test 2", "Test 3"]
    for text in texts:
        analyzer.analyze(text)
    
    insights = analyzer.get_recent_insights(limit=2)
    assert len(insights) == 2
    assert insights[0]["text"] == texts[-1]  # Most recent first