FROM asia-south1-docker.pkg.dev/robotshop-platform-dev/baseimages/python:3.14.7-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

EXPOSE 9000

CMD ["adk", "api_server", "--host", "0.0.0.0", "--port", "9000", "src"]