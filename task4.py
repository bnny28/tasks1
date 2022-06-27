from itertools import combinations as cmb


def bananas(s: str) -> set:
    """
    :param s: the string possibly containing the word banana
    :return: the set of banana words found in the string
    """
    result = set()
    lngth = len(s)
    b_start_search = 0
    # Проверяем слово на размер
    if lngth >= 6:
        # Генерируем комбинации позиций на которых могут стоять "-"
        for combs_pos in cmb(range(lngth), lngth - 6):
            # Для текущей комбинации заменяем в слове буквы в позициях на "-"
            lst_word = list(s)
            for i in combs_pos:
                lst_word[i] = '-'
            variant = ''.join(lst_word)
            # Проверяем получилось ли слово "bananas"
            # Если да, добавляем в результирующий набор
            if variant.replace('-', '') == 'banana':
                result.add(variant)
    return result


if __name__ == '__main__':
    # Самопроверки
    assert bananas("") == set()
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
    print('\nПроверки пройдены!')

    print('\nПример работы:')
    s = 'bbananana'
    print(f'Кол-во слов banana в {s} -> {len(bananas(s))} \n {bananas(s)}')
