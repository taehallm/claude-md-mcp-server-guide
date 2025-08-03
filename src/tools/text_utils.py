"""Text utility tools for string manipulation and analysis."""

from typing import Any, Dict


def count_words(text: str) -> Dict[str, Any]:
    """Count words, characters, and lines in the provided text."""
    lines = text.split("\n")
    words = text.split()
    chars = len(text)
    chars_no_spaces = len(text.replace(" ", ""))

    return {
        "text_length": len(text),
        "word_count": len(words),
        "character_count": chars,
        "character_count_no_spaces": chars_no_spaces,
        "line_count": len(lines),
        "average_words_per_line": len(words) / len(lines) if lines else 0,
    }


def reverse_text(text: str) -> Dict[str, str]:
    """Reverse the provided text."""
    return {"original": text, "reversed": text[::-1]}
