def domain_name(url: str) -> str:
    """
    :param url: typical url
    :return: domain from url
    """
    # 'Очищаем' начало, если нужно, с приведением url в нижний регистр
    lower_url = url.strip().lower()
    if 'www.' in lower_url:
        token = lower_url.split('www.')[1]
    elif '//' in lower_url:
        token = lower_url.split('//')[1]
    else:
        token = lower_url

    # Домен -> строка до первой точки
    return token.split('.')[0]


if __name__ == '__main__':
    # Самопроверки
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
    assert domain_name("http://github.com/carbonfive/raygun") == "github"
    assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
    assert domain_name("HTTPS://WWW.CNET.COM") == "cnet"
    print('\nПроверки пройдены!')

    print('\nПример работы:')
    print(f'Домен из url "http://google.com" -> {domain_name("http://google.com")}')
