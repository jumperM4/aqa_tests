# test_logger_demo.py
from logger_config import logger

def test_logger_outputs():
    logger.debug("🧪 Это DEBUG-сообщение — для отладки.")
    logger.info("ℹ️ Это INFO-сообщение — обычная информация.")
    logger.warning("⚠️ Это WARNING — что-то может быть не так.")
    logger.error("❌ Это ERROR — что-то пошло не так.")
    logger.critical("🔥 Это CRITICAL — всё сломалось!")
