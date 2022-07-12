import time


def delay_decorator_runner(call_count, start_sleep_time, factor, boarder_sleep_time):
    """
    Вычисляет функцию заданное количество раз с задержкой, определяемой по правилам:

    t = start_sleep_time * 2^(factor) if t < border_sleep_time
    t = border_sleep_time if t >= border_sleep_time.

    :param call_count: количество запусков функции
    :param start_sleep_time: начальное время ожидания
    :param factor: параметр для вычисления задержки
    :param boarder_sleep_time: граничное время ожидания
    :return: функция-декоратор
    """
    def delay_decorator_exponent_time(func):
        def wrapper(*args, **kwargs):
            t = start_sleep_time
            print(f'Кол-во запусков = {call_count}')
            print('Начало работы')
            for num in range(1, call_count + 1):
                function_result = func(*args, **kwargs)
                print(f'Запуск номер {num}. Ожидание: {t} секунд. Результат декорируемой функции = {function_result}.')
                time.sleep(t)
                calc_time = t * (2 ** factor)
                t = boarder_sleep_time if calc_time > boarder_sleep_time else calc_time
            print('Конец работы')

        # Не используем библиотеку wraps из functools, переопределяем документацию вручную
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper

    return delay_decorator_exponent_time


@delay_decorator_runner(call_count=3, start_sleep_time=1, factor=2, boarder_sleep_time=10)
def multiplier(number: int):
    """
    Multiplies by 2.

    :param number: multipliable number
    :return: result of multiplication
    """

    return number * 2


if __name__ == '__main__':
    multiplier(2)
