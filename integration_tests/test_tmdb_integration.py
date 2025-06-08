import pytest
from api.api_client import TMDB_client
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.integration
def test_get_popular_movies_real_api():
    client = TMDB_client(
        base_url=os.getenv("BASE_URL"),
        api_key=os.getenv("KEY_TO_API_ACCESS")
    )

    data = client.get_popular_movies(language="en-US", page="1")

    assert "results" in data
    assert isinstance(data["results"], list)
    assert len(data["results"]) > 0


# ▶️ Шаг 3: Как запускать
# Чтобы не запускать вместе с юнитами: pytest -m integration

# А юниты без интеграции: pytest -m "not integration"
