"""Calculator tools for basic mathematical operations."""

from datetime import datetime
from typing import Any, Dict


def add_numbers(a: float, b: float) -> Dict[str, Any]:
    """Add two numbers and return the result."""
    result = a + b
    return {
        "operation": "addition",
        "operands": [a, b],
        "result": result,
        "timestamp": datetime.now().isoformat(),
    }


def multiply_numbers(a: float, b: float) -> Dict[str, Any]:
    """Multiply two numbers and return the result."""
    result = a * b
    return {
        "operation": "multiplication",
        "operands": [a, b],
        "result": result,
        "timestamp": datetime.now().isoformat(),
    }
