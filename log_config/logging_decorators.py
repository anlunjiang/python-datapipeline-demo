import logging
import time
from functools import update_wrapper

from log_config.loggingconf import logger


def log_with_time(level: int = logging.DEBUG):
    def decorator(method):
        def wrapper(*args, **kwargs):
            ts = time.time()
            logger.log(level=level, msg=f"timing started for method: {method.__name__}")
            ret = method(*args, **kwargs)
            logger.log(level=level, msg=f"time taken {round(time.time() - ts, 3)}s")
            return ret

        update_wrapper(wrapper=wrapper, wrapped=method)

        return wrapper

    return decorator
