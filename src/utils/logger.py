from loguru import logger
import sys

logger.remove()  # remove default config

logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "<cyan>{name}</cyan> | "
           "{message}",
    level="INFO",)


logger.add(
    "logs/app.log",
    rotation="1 MB",
    retention="7 days",
    compression="zip",
    level="INFO",)

# includes all
__all__ = ["logger"]


