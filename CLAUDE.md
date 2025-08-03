# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Type

This is an MCP (Model Context Protocol) Server project built with Python using UV package manager and FastMCP framework.

For additional documentation and examples, refer to the official MCP Python SDK: https://github.com/modelcontextprotocol/python-sdk

## Development Setup

### Prerequisites
- UV package manager (replaces pip/conda)
- Python 3.10+ (required by MCP)

### Common Development Commands
```bash
# Install dependencies
uv add "mcp[cli]"

# Run server directly (runs silently, no output)
uv run mcp run server.py

# Run server in development mode with MCP Inspector UI
uv run mcp dev server.py

# Install server in Claude Desktop
uv run mcp install server.py

# List available MCP commands
uv run mcp --help

# Check MCP version
uv run mcp version

# Run tests
uv run pytest

# Format code
uv run ruff format .

# Lint code  
uv run ruff check .
```

## MCP Server Architecture

### Project Structure

#### Option 1: Simple Structure (Direct Decorators)
```
project/
├── server.py           # All tools/resources defined here
├── pyproject.toml     # UV project configuration
├── tests/             # Test files
└── README.md          # Server documentation
```

#### Option 2: Modular Structure (Manual Registration) - Recommended
```
project/
├── server.py           # Main MCP server entry point
├── pyproject.toml     # UV project configuration
├── src/               # Server implementation modules
│   ├── tools/         # MCP tool implementations
│   ├── resources/     # MCP resource implementations
│   └── prompts/       # MCP prompt implementations
├── tests/             # Test files
└── README.md          # Server documentation
```

### FastMCP Development Patterns

#### Server Definition
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("server-name")
# No if __name__ == "__main__" needed - MCP CLI handles execution
```

#### Approach 1: Direct Decorators (Simple/Monolithic)
All tools/resources defined in server.py with decorators:
```python
@mcp.tool()
def tool_name(param: str) -> dict:
    """Clear description of what this tool does."""
    return {"result": "value"}

@mcp.resource("resource://name")
def resource_name() -> str:
    """Resource description."""
    return "resource content"
```

#### Approach 2: Modular with Manual Registration (Recommended)
Tools/resources in separate modules, registered in server.py:

**In src/tools/example.py:**
```python
def tool_name(param: str) -> dict:
    """Clear description of what this tool does."""
    return {"result": "value"}
```

**In server.py:**
```python
from src.tools.example import tool_name
from src.resources.info import resource_name

# Register tools and resources
mcp.tool()(tool_name)
mcp.resource("resource://name")(resource_name)
```

#### Code Organization Principles
- Use type hints extensively for better IDE support and validation
- Provide comprehensive docstrings for all tools, resources, and prompts
- Handle errors gracefully and return meaningful error messages
- Use Pydantic models or TypedDicts for structured data
- Don't include `if __name__ == "__main__":` blocks - MCP CLI handles server execution

**For Simple Structure:**
- Keep all tools/resources in server.py using decorators
- Good for small servers with few tools

**For Modular Structure:**
- Group related functionality into separate modules under `src/`
- Import and manually register with `mcp.tool()(function_name)`
- Better for larger servers with many tools/resources
- Easier testing and maintenance

## Development Workflow

### Server Development Cycle
1. Implement tools/resources/prompts with proper type hints and docstrings
2. Test server directly: `uv run mcp run server.py` (runs silently and nothing streams on the terminal when runned properly)
3. Test with MCP Inspector UI: `uv run mcp dev server.py` (opens web interface)
4. Run linting and formatting: `uv run ruff check . && uv run ruff format .`
5. Run tests: `uv run pytest`
6. Install in Claude Desktop: `uv run mcp install server.py`

### Testing MCP Servers

#### Automated Testing (Claude Code can help with):
- Write unit tests for individual tools and resources
- Test error handling and edge cases
- Validate JSON schema compliance for structured outputs
- Run tests with `uv run pytest`

#### Manual/Interactive Testing (User must do):
- Use `uv run mcp dev server.py` to open MCP Inspector web UI
- Test tools interactively in the browser interface
- Verify tool/resource behavior with real inputs
- Check server capabilities and metadata

#### Notes:
- `uv run mcp run server.py` runs silently with no output
- Claude Code can write automated tests but cannot interact with the MCP Inspector UI
- For development, combine both automated tests and manual Inspector testing manually

### Configuration Management
- Define server metadata in FastMCP constructor
- Use environment variables for sensitive configuration
- Implement proper async context management for resources
- Handle server lifecycle with `asynccontextmanager` when needed

### Best Practices
- Keep tool functions focused and single-purpose
- Use descriptive names that clearly indicate functionality
- Implement proper error handling with informative messages
- Validate inputs and sanitize outputs
- Document expected input/output formats in docstrings