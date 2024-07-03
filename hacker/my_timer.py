import logging
import time
from contextlib import contextmanager

logging.basicConfig(level=logging.INFO)
log = logging.Logger("my_timer")

# function for use in context


@contextmanager
def cm_timer(label):
    """context manager timer.  Yields before the thing being timed is executed."""
    log.info("entered cm_timer context")
    start_time = time.time()
    log.info("yielding to function to run")
    yield
    log.info("after yielding, now back in cm_timer")
    print(f"{label}: {time.time() - start_time:.06f} seconds")


# decorator
def dec_timer(func):
    def wrapper_timer(*arg, **kwargs):
        with Timer(func.__name__):
            return func(*arg, **kwargs)

    return wrapper_timer


# Class for use in context
class Timer(object):
    """Purpose: create a timer object that can be used in context to time arbitrary sets of statements
    Parameters:
    description: str, description echoed in the logging of the elapsed time
    """

    def __init__(self, description="Timer."):
        self.description = description

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"{self.description}: {time.time() - self.start_time:.06f} seconds")
