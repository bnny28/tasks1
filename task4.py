import re


def bananas(s: str) -> set:
    """
    :param s: the string possibly containing the word banana
    :return: the set of banana words found in the string
    """
    # Не ругайтесь, пожалуйста )) Не знаю как красиво зарефакторить. Возможно что-то с itertools
    result = set()
    b_start_search = 0
    for b_matcher in re.finditer('b', s[b_start_search:]):
        b_pos = b_matcher.start()
        a1_start_search = b_pos + 1
        s_without_b = s[:b_pos] + '-' + s[b_pos + 1:]
        for a1_matcher in re.finditer('a', s_without_b[a1_start_search:]):
            a1_pos = a1_start_search + a1_matcher.start()
            n1_start_search = a1_pos + 1
            s_without_ba = s_without_b[:a1_pos] + '-' + s_without_b[a1_pos + 1:]
            for n1_matcher in re.finditer('n', s_without_ba[n1_start_search:]):
                n1_pos = n1_start_search + n1_matcher.start()
                a2_start_search = n1_pos + 1
                s_without_ban = s_without_ba[:n1_pos] + '-' + s_without_ba[n1_pos + 1:]
                for a2_matcher in re.finditer('a', s_without_ban[a2_start_search:]):
                    a2_pos = a2_start_search + a2_matcher.start()
                    n2_start_search = a2_pos + 1
                    s_without_bana = s_without_ban[:a2_pos] + '-' + s_without_ban[a2_pos + 1:]
                    for n2_matcher in re.finditer('n', s_without_bana[n2_start_search:]):
                        n2_pos = n2_start_search + n2_matcher.start()
                        a3_start_search = n2_pos + 1
                        s_without_banan = s_without_bana[:n2_pos] + '-' + s_without_bana[n2_pos + 1:]
                        for a3_matcher in re.finditer('a', s_without_banan[a3_start_search:]):
                            a3_pos = a3_start_search + a3_matcher.start()
                            s_without_banana = s_without_banan[:a3_pos] + '-' + s_without_banan[a3_pos + 1:]
                            variant_banana = ''.join(
                                [v if k == '-' else '-' for k, v in zip(s_without_banana, s)])
                            result.add(variant_banana)
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
