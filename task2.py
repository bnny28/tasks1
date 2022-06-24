def int32_to_ip(int32: int) -> str:
    """
    :param int32: numerical representation of ip
    :return: string ip
    """
    # Генерируем список, состоящий из 4 элементов ip адреса,
    # формируемых битовыми операциями сдвига,
    # а затем битовым И с числом 11111111 (0xFF)
    # Это позволяет получить список строк элементов ip адреса,
    # расположенных в обратном порядке
    invert_ip_list = [str(int32 >> (i << 3) & 0xFF) for i in range(0, 4)]
    # Инвертируем список, для исправления порядка следования
    ip_list = invert_ip_list[::-1]
    # 'Склеиваем' список через точку в строковое значение ip
    return '.'.join(ip_list)


if __name__ == '__main__':
    # Самопроверки
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(32) == "0.0.0.32"
    assert int32_to_ip(2149583361) == "128.32.10.1"
    print('\nПроверки пройдены!')

    print('\nПример работы:')
    print(f'IP из числа 32 -> {int32_to_ip(32)}')