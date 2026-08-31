import os

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

from gcp_infra_agent.src.prompts.system_instruction import SYSTEM_INSTRUCTION
from gcp_infra_agent.src.mcp.github import create_github_mcp_toolset


LITELLM_PROXY_URL = os.environ["LITELLM_PROXY_URL"]
LITELLM_PROXY_API_KEY = os.environ["LITELLM_PROXY_API_KEY"]
VERTEX_AI_MODEL = os.environ["VERTEX_AI_MODEL"]


model = LiteLlm(
    model=f"openai/{VERTEX_AI_MODEL}",
    api_base=f"{LITELLM_PROXY_URL}/v1",
    api_key=LITELLM_PROXY_API_KEY,
)


root_agent = LlmAgent(
    model=model,
    name="robotshop_infra_assistant",
    description=(
        "Read-only assistant that inspects the Robotshop Terraform "
        "repository via the GitHub MCP server and explains its "
        "infrastructure configuration."
    ),
    instruction=SYSTEM_INSTRUCTION,
    tools=[create_github_mcp_toolset()],
)
