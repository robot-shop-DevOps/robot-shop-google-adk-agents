import os
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

from gcp_infra_agent.prompts.system_instruction import SYSTEM_INSTRUCTION
from gcp_infra_agent.mcp.github import create_github_mcp_toolset
from gcp_infra_agent.mcp.gcp import create_gcp_mcp_toolset
from gcp_infra_agent.auth.cloudrun_token import TokenManager


LITELLM_PROXY_URL = os.environ["LITELLM_PROXY_URL"]
LITELLM_PROXY_API_KEY = os.environ["LITELLM_PROXY_API_KEY"]
VERTEX_AI_MODEL = os.environ["VERTEX_AI_MODEL"]

token_manager = TokenManager(
    target_audience_url = LITELLM_PROXY_URL
)

id_token = token_manager.get_token()

model = LiteLlm(
    model=f"openai/{VERTEX_AI_MODEL}",
    api_base=f"{LITELLM_PROXY_URL}/v1",
    api_key=LITELLM_PROXY_API_KEY,
    extra_headers={
        "X-Serverless-Authorization": f"Bearer {id_token}"
    }
)


root_agent = LlmAgent(
    model=model,
    name="robotshop_infra_assistant",
    description=(
        "Read-only assistant that inspects the Robotshop Terraform "
        "repository via GitHub MCP and the deployed GCP infrastructure "
        "via GCP MCP, and explains the infrastructure configuration."
    ),
    instruction=SYSTEM_INSTRUCTION,
    tools=[
        create_github_mcp_toolset(),
        create_gcp_mcp_toolset()
    ],
)
