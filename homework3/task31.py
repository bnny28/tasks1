def cache_decorator_in_dict(func):
    """
    Decorator for caching the result of function execution.

    :param func: cached function
    :return: result of the function execution
    """

    cache = dict()

    def wrapper(*args, **kwargs):
        if f'{args, kwargs}' not in cache:
            cache[f'{args, kwargs}'] = func(*args, **kwargs)
        return cache[f'{args, kwargs}']

    # Не используем библиотеку wraps из functools, переопределяем документацию вручную
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


@cache_decorator_in_dict
def multiplier(number: int):
    """
    Multiplies by 2.

    :param number: multipliable number
    :return: result of multiplication
    """

    return number * 2


if __name__ == '__main__':
    pass
