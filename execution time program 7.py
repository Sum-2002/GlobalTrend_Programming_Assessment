import time
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"Function {func.__name__} took {execution_time:.2f} seconds to execute")
        return result
    return wrapper


@timer_decorator
def expensive_task(n):
    result = 0
    for i in range(n):
        result += i ** 2
    return result


expensive_task(1000000)