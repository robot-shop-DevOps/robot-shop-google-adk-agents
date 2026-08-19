import os
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams


GITHUB_MCP_URL = "https://api.githubcopilot.com/mcp/readonly"

READ_ONLY_TOOL_NAMES = [
    "get_me",
    "search_repositories",
    "search_code",
    "get_file_contents",
    "get_repository_tree",
    "list_branches",
    "list_commits",
    "get_commit",
    "list_tags",
    "list_releases",
    "get_latest_release",
]

def get_github_token() -> str:
    token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")

    if not token:
        raise RuntimeError(
            "GITHUB_PERSONAL_ACCESS_TOKEN environment variable is not set."
        )

    return token


def create_github_mcp_toolset() -> McpToolset:
    token = get_github_token()

    return McpToolset(
        connection_params=StreamableHTTPConnectionParams(
            url=GITHUB_MCP_URL,
            headers={
                "Authorization": f"Bearer {token}",
                "X-MCP-Toolsets": "context,repos,git",
                "X-MCP-Readonly": "true",
            },
        ),
        tool_filter=READ_ONLY_TOOL_NAMES,
    )