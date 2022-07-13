from abc import ABC, abstractmethod

from heroes import ABCHero
from places import ABCPlace


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
        point = 'planet ' + str(place.coordinates) if place.is_planet else place.name

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
