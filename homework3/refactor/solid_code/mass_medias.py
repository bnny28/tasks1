from abc import ABC, abstractmethod
from typing import Union

from heroes import ABCHero
from places import ABCPlanet, ABCCity


class ABCMedia(ABC):
    """
    Абстрактный класс средства массовой информации.
    """
    @abstractmethod
    def create_news(self, place: Union[ABCPlanet, ABCCity], hero: ABCHero):
        pass


class NewsPapers(ABCMedia):
    """
    Класс газет.
    """
    def create_news(self, place: Union[ABCPlanet, ABCCity], hero: ABCHero):
        """
        Выпуск новостей.

        :param place: место события
        :param hero: герой
        :return: Null
        """
        point = place.name if isinstance(place, ABCCity) else 'planet ' + str(place.coordinates)
        print(f'{hero.name} saved the {point}!')
