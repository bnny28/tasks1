from abc import ABC, abstractmethod

from heroes import ABCHero
from places import ABCPlanet, ABCCity, ABCPlace


class ABCMedia(ABC):
    """
    Абстрактный класс средства массовой информации.
    """
    @abstractmethod
    def create_news(self, place: ABCPlace, hero: ABCHero):
        """
        Выпуск новостей.

        :param place: место события
        :param hero: герой
        :return: Null
        """
        point = place.name if isinstance(place, ABCCity) else 'planet ' + str(place.coordinates) \
            if isinstance(place, ABCPlanet) else 'unknown'
        return f'{hero.name} saved the {point}!'


class NewsPapers(ABCMedia):
    """
    Класс газет.
    """
    def create_news(self, place: ABCPlace, hero: ABCHero):
        print(f'NewsPapers: {super().create_news(place, hero)}')


class Radio(ABCMedia):
    """
    Класс радио.
    """
    def create_news(self, place: ABCPlace, hero: ABCHero):
        print(f'Radio: {super().create_news(place, hero)}')
