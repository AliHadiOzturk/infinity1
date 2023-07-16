import logging
import sys
from .config import Config


config: Config = Config().load()

logging.basicConfig(level=logging.getLevelName(config.LOG_LEVEL), stream=sys.stdout)
logging.info("Configuration loaded")

logging.info(f"APP NAME: ${config.APP_NAME}")

logger = logging