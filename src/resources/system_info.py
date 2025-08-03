"""System information resources."""

import platform
import sys
from datetime import datetime


def get_system_info() -> str:
    """Get basic system information."""
    info = {
        "platform": platform.platform(),
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": sys.version,
        "timestamp": datetime.now().isoformat(),
    }

    return f"""System Information:
Platform: {info['platform']}
System: {info['system']} {info['release']}
Machine: {info['machine']}
Processor: {info['processor']}
Python Version: {info['python_version']}
Generated: {info['timestamp']}"""


def get_server_status() -> str:
    """Get current server status and capabilities."""
    return f"""MCP Server Status:
Server Name: sample-server
Status: Running
Available Tools: 4 (add_numbers, multiply_numbers, count_words, reverse_text)
Available Resources: 2 (system://info, server://status)
Python Version: {sys.version.split()[0]}
Timestamp: {datetime.now().isoformat()}"""
