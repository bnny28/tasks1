def zeros(n: int) -> int:
    """
    :param n: the number to calculate the factorial
    :return: the number of terminating zeros in the calculated factorial
    """
    # Факториал числа n равен произведению чисел от 1 до n.
    # Ноль в конце произведения появляется в результате перемножения 2 и 5.
    # Но поскольку при разложении на простые множители числа n! двоек больше чем пятерок,
    # то количество нулей в конце n! равно количеству пятерок
    # в разложении n! на простые множители.
    res = 0
    while n > 0:
        n //= 5
        res += n
    return res


if __name__ == '__main__':
    # Самопроверки
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
    print('\nПроверки пройдены!')

    print('\nПример работы:')
    print(f'Кол-во завершающих нулей в факториале от 6 -> {zeros(6)}')
