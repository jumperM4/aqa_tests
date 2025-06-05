import pytest
from api.api_client import TMDB_client
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.integration
def test_get_popular_movies_real_api():
    client = TMDB_client(
        base_url=os.getenv("base_url"),
        api_key=os.getenv("key_to_API_access")
    )

    data = client.get_popular_movies(language="en-US", page="1")

    assert "results" in data
    assert isinstance(data["results"], list)
    assert len(data["results"]) > 0


# ▶️ Шаг 3: Как запускать
# Чтобы не запускать вместе с юнитами: pytest -m integration

# А юниты без интеграции: pytest -m "not integration"
