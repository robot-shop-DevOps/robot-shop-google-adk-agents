FROM asia-south1-docker.pkg.dev/robotshop-platform-dev/baseimages/python:3.14.7-slim

WORKDIR /gcp_infra_agent

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY gcp_infra_agent/ ./gcp_infra_agent/

EXPOSE 9000

CMD ["adk", "api_server", "--host", "0.0.0.0", "--port", "9000", "gcp_infra_agent"]