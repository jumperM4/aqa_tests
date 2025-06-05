import pytest

from api.api_client import TMDB_client
import itertools


# Иногда тебе нужно сгенерировать все возможные комбинации нескольких параметров. Используем itertools.product
# languages = ["en-US", "ru-RU"]
# pages = [1, 2]
# @pytest.mark.parametrize(
#     "language,page",
#     list(itertools.product(languages, pages))
# )

@pytest.mark.parametrize("language,page", [
    ("en-US", "1"),
    # ("fr-FR", "1"),
    ("ru-RU", "1")
],
                         ids=["english", "russian"]  # Чтобы видеть читаемые названия тестов в выводе
                         )
def test_get_popular_movies(tmdb_client, language, page):
    data = tmdb_client.get_popular_movies(page=page, language=language)

    print(data)
    assert "results" in data
    assert isinstance(data["results"], list)
    assert len(data["results"]) > 0

    first_movie = data["results"][0]
    assert "title" in first_movie
    assert isinstance(first_movie["title"], str)
