import time
import threading
import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import id_token


TOKEN_REFRESH_INTERVAL = 45 * 60

class TokenManager:
    def __init__(self, target_audience_url: str):
        self.target_audience_url = target_audience_url
        self._token = None
        self._created_at = 0
        self._lock = threading.Lock()

    def _generate_token(self) -> str:
        credentials, project = google.auth.default()
        auth_req = Request()

        return id_token.fetch_id_token(
            auth_req,
            self.target_audience_url,
        )

    def get_token(self) -> str:
        with self._lock:
            now = time.monotonic()

            if self._token and (now - self._created_at) < TOKEN_REFRESH_INTERVAL:
                return self._token

            self._token = self._generate_token()
            self._created_at = now

            return self._token
