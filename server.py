#!/usr/bin/env python3
"""
Simple MCP Server built with FastMCP.

This server provides basic tools and resources for demonstration purposes.
"""

from mcp.server.fastmcp import FastMCP

from src.tools.calculator import add_numbers, multiply_numbers
from src.tools.text_utils import count_words, reverse_text
from src.resources.system_info import get_system_info, get_server_status

# Initialize the MCP server
mcp = FastMCP("sample-server")

# Register tools
mcp.tool()(add_numbers)
mcp.tool()(multiply_numbers)
mcp.tool()(count_words)
mcp.tool()(reverse_text)

# Register resources
mcp.resource("system://info")(get_system_info)
mcp.resource("server://status")(get_server_status)
