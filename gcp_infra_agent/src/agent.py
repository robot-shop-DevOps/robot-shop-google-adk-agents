from google.adk.agents import LlmAgent

from gcp_infra_agent.src.prompts.system_instruction import SYSTEM_INSTRUCTION
from gcp_infra_agent.src.mcp.github import create_github_mcp_toolset

root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="robotshop_infra_assistant",
    description=(
        "Read-only assistant that inspects the Robotshop Terraform"
        "repository via the GitHub MCP server and explains its"
        "infrastructure configuration."
    ),
    instruction=SYSTEM_INSTRUCTION,
    tools=[create_github_mcp_toolset()],
)
