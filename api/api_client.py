import requests

class TMDB_client:

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def _make_request(self, endpoint: str, params: dict = None) -> dict:
        # _make_request() — универсальный приватный метод, весь API клиента теперь строится на нём.
        # Используем endpoint как часть URL.
        # При ошибке выбрасывается TMDbAPIError.
        """Универсальный метод для GET-запросов к TMDb API."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.get(url=url, headers=self.headers, params=params)
        if response.status_code != 200:
            try:
                error_msg = response.json().get("status_message", "Unknown error")
            except Exception:
                error_msg = response.text
            raise TMDbAPIError(status_code=response.status_code, message=error_msg)

            # Можно кастомизировать это, но пока просто выбросим Exception
            # raise Exception(f"TMDb API error {response.status_code}: {response.json().get('status_message')}")

        # response.raise_for_status()
        return response.json()


    def get_popular_movies(self, page: str = 1, language: str = 'en-US'):
        return self._make_request(endpoint="movie/popular", params={
            "page": page,
            "language": language
        })


class TMDbAPIError(Exception):
    """Базовое исключение для ошибок TMDb API."""

    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"[{status_code}] {message}")
#  Объяснение:
# Храним и status_code, и message — полезно для логирования и отладки.
# Наследуемся от Exception, так что всё стандартно.
# super().__init__() задаёт, что будет видно в str(e).