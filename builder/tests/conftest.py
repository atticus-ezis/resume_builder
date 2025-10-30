"""
Pytest configuration and fixtures for builder tests.
"""
import pytest
from pathlib import Path

# Get the tests directory path
TESTS_DIR = Path(__file__).parent


@pytest.fixture
def sample_markdown_file():
    """Load the sample markdown file for testing."""
    md_file = TESTS_DIR / "sample_md.md"
    with open(md_file, "r", encoding="utf-8") as f:
        return f.read()



