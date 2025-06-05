# 1. Базовый образ с Python
FROM python:3.11-slim

# 2. Установим рабочую директорию
WORKDIR /app

# 3. Скопируем зависимости и установим их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Скопируем весь проект в контейнер
COPY . .

# Гарантируем, что папка логов есть
RUN mkdir -p /app/logs

# 5. Установим переменные окружения (для dotenv или ручной подмены)
ENV PYTHONUNBUFFERED=1

# Запуск тестов
CMD ["pytest", "--tb=short", "--disable-warnings"]


# Сборка образа
# docker build -t tmdb-tests .
# Запуск контейнера (запустит pytest)
# docker run --rm --env-file .env tmdb-tests
