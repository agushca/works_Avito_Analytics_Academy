import time
from random import randint


def log(template):
    """
    A decorator logging the function execution time with a provided template.
    Args:
        template: A string template that will be used to format the log.
        The template must include a `{}` placeholder for the execution time.
    Returns:
        A decorator function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(template.format(randint(1, 5)))
            return result
        return wrapper
    return decorator