import pytest
from unittest.mock import patch, Mock
from api.api_client import TMDB_client, TMDbAPIError

@patch("api.api_client.requests.get")
def test_get_popular_movies_success(mock_get):
    # настраиваем mock ответов
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "results": [
            {"title": "Movie 1"},
            {"title": "Movie 2"},
        ]
    }
    print("1", mock_get)
    print("2", mock_response)
    mock_get.return_value = mock_response

    # 2. Создаем экземпляр клиента
    client = TMDB_client(base_url="https://fake.url", api_key="FAKE_KEY")

    # 3. Вызываем метод
    result = client.get_popular_movies(language="en-US", page="1")

    # 4. Проверяем результат
    assert "results" in result
    assert len(result["results"]) == 2
    assert result["results"][0]["title"] == "Movie 1"

    print("3", mock_get.call_args)
    # 5. Проверяем, что get вызван правильно
    mock_get.assert_called_once_with(
        url="https://fake.url/movie/popular",
        params={"page": "1", "language": "en-US"},
        headers={'accept': 'application/json', 'Authorization': 'Bearer FAKE_KEY'}
    )

@patch("api.api_client.requests.get")
def test_get_popular_movies_unauthorized(mock_get):
    # 1. Настраиваем фейловый ответ
    mock_response = Mock()
    mock_response.status_code = 401
    mock_response.json.return_value = {"status_message": "Invalid API key"}
    mock_get.return_value = mock_response

    # 2. Создаем экземпляр клиента
    client = TMDB_client(base_url="https://fake.url", api_key="INVALID_KEY")

    # 3. Проверка реакции на ошибку (предположим, клиент выбрасывает ошибку)
    with pytest.raises(Exception) as exc_info:
        result = client.get_popular_movies(language="en-US", page="1")

    # result = client.get_popular_movies(language="en-US", page="1")
    # assert result.get("status_message") == "Invalid API key"

    # 4. Убеждаемся, что сообщение об ошибке есть
    assert exc_info.value.status_code == 401
    assert "Invalid API key" in str(exc_info.value)


@patch("api.api_client.requests.get")
def test_get_popular_movies_server_error(mock_get):
    # 1. Подделка ответа с ошибкой 500
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.json.return_value = {"status_message": "Internal server error"}
    mock_get.return_value = mock_response

    client = TMDB_client(base_url="https://fake.url", api_key="FAKE_KEY")

    # 3. Проверка: выбрасывается ли исключение
    with pytest.raises(Exception) as exc_info:
        client.get_popular_movies(page="1", language="en-US")

    print("1", exc_info.value)
    assert "500" in str(exc_info.value)
    assert "Internal server error" in str(exc_info.value)

