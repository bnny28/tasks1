import math


def zeros(n: int) -> int:
    """
    :param n: the number to calculate the factorial
    :return: the number of terminating zeros in the calculated factorial
    """
    s = str(math.factorial(n))
    # Вычисляем разницу длин строк между полным значением и
    # с отброшенными нулями справа
    return len(s) - len(s.rstrip('0'))


if __name__ == '__main__':
    # Самопроверки
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
    print('\nПроверки пройдены!')

    print('\nПример работы:')
    print(f'Кол-во завершающих нулей в факториале от 6 -> {zeros(6)}')
