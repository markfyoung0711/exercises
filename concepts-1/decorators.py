import functools
import logging
import time
from enum import Enum


class IntegrityCheckMode(Enum):
    """Integrity check mode for identifying level of criticality"""

    CRITICAL = "critical"
    WARNING = "warning"


logging.basicConfig(level=logging.INFO)
log = logging.getLogger("decorators")


def critical_check(vendor: list, descriptors, message2):
    """Template for decorator that takes arguments in order to use those arguments
    to affect the way the enclosed decorator or wrapper function behaves"""

    mode = IntegrityCheckMode.CRITICAL

    def decorator(fun):

        def wrapper(*args, **kwargs):
            if vendor not in kwargs["vendor"]:
                log.info(f"matching 'critical_check' mode is {mode}")
                return fun(*args, **kwargs)
            return None

        return wrapper

    return decorator


# decorator template - start with this for a simple decorator
def noarg_decorator_template(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value

    return wrapper_decorator


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value

    return wrapper_timer


# decorators
def debug(f):
    """Purpose: debug a function"""

    def wrapper_debug(*args, **kwargs):
        log.info("in the wrapper")
        return f(*args, **kwargs)

    return wrapper_debug


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice
