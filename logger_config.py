# logger_config.py
import logging
import sys
from pathlib import Path
# logging — стандартная библиотека Python для логирования.
# sys.stdout — нужен, чтобы направить вывод логов в консоль.
# Path — модуль для удобной работы с путями к файлам и папкам.


# Путь к лог-файлу
LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "test_log.log"
# Path(__file__).parent — путь до папки, где находится этот скрипт.
# / "logs" — создаём путь до папки logs.
# .mkdir(exist_ok=True) — создаёт папку logs, если она ещё не существует.
# Формируем путь до лог-файла, например: ./logs/test_log.log

# Настройка логгера
logger = logging.getLogger("tmdb_logger")
logger.setLevel(logging.DEBUG)
# Создаём именованный логгер "tmdb_logger" (можно использовать в любом файле через getLogger("tmdb_logger"))
# .setLevel(logging.DEBUG) — разрешаем логировать все уровни сообщений от DEBUG и выше (INFO, WARNING, ERROR, CRITICAL)

# Формат логов
formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s", "%H:%M:%S")
# Пример вывода: [14:22:31] INFO: Запрос успешно отправлен

# Хендлер: stdout
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
# StreamHandler(sys.stdout) — отправляет логи в консоль.
# setFormatter(...) — применяем наш формат.
# addHandler(...) — подключаем обработчик к логгеру.

# Хендлер: файл
file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
# FileHandler(...) — логирует в файл logs/test_log.log.
# Кодировка utf-8, чтобы корректно записывать кириллицу.
# И тоже подключаем обработчик к логгеру.
