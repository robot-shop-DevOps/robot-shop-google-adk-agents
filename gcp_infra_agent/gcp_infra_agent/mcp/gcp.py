import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import id_token

from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams


GCP_MCP_URL = "https://run.googleapis.com/mcp"


READ_ONLY_TOOL_NAMES = [
    "get_service",
    "list_services",
]

def get_adc_token() -> str:
    credentials, _ = google.auth.default()
    auth_req = Request()

    return id_token.fetch_id_token(
        auth_req,
        self.target_audience_url,
    )

def create_gcp_mcp_toolset() -> McpToolset:
    token = get_adc_token()
    
    return McpToolset(
        connection_params=StreamableHTTPConnectionParams(
            url=GCP_MCP_URL,
            headers={
                "Authorization": f"Bearer {token}",
            },
        ),
        tool_filter=READ_ONLY_TOOL_NAMES,
    )