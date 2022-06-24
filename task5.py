def count_find_num(primesL: list, limits: int) -> list:
    """
    :param primesL: list of prime factors
    :param limits: limit of the mathematical product
    :return: the list of the number of mathematical products and the maximum value of them
    """
    # Перемножим простые множители
    product = 1
    for multiplier in primesL:
        product *= multiplier
    # Если произведение больше лимита вернем пустой результат
    if product > limits:
        return []
    # Создадим список результатов произведений
    products = [product]
    # Для каждого значения в списке результатов получаем новый, умножая
    # на каждый из простых множителей столько раз, пока не превысим limits.
    # Добавляем результат в список, если еще нет
    for item in products:
        for multiplier in primesL:
            new_product = item * multiplier
            while new_product <= limits:
                if new_product not in products:
                    products.append(new_product)
                new_product *= multiplier

    return [len(products), max(products)]


if __name__ == '__main__':
    # Самопроверки
    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]
    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]
    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]
    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]
    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []
    print('\nПроверки пройдены!')

    print('\nПример работы:')
    primesL = [2, 3, 5]
    limit = 500
    print(f'Для primesL = {primesL} и limit = {limit} -> {count_find_num(primesL, limit)}')
