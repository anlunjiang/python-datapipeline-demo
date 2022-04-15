import logging

logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger()
