import logging
import sys
from .exception import Exceptions, GenericException
from .config import Config


config: Config = Config().load()

logging.basicConfig(level=logging.getLevelName(config.LOG_LEVEL), stream=sys.stdout)
logging.info("Configuration loaded")

logging.info(f"APP NAME: {config.APP_NAME}")

fh = logging.FileHandler('log.txt')
fh.setLevel(logging.getLevelName(config.LOG_LEVEL))

logger = logging.getLogger()

logger.addHandler(fh)