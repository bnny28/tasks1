from abc import ABC, abstractmethod

from weapons import Lasers, Gun


class ABCHero(ABC):
    """
    Абстрактный класс героя с обычной атакой.
    """
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @staticmethod
    def find(place):
        return place.get_antagonist()


class ABCSuperHero(ABCHero):
    """
    Абстрактный класс супергероя, который обладает максимальной атакой.
    """
    @abstractmethod
    def ultimate(self):
        pass


class Superman(ABCSuperHero, Lasers):
    name = 'Clark Kent'

    def attack(self):
        print('Kick')

    def ultimate(self):
        self.use_weapon()


class ChuckNorris(ABCHero, Gun):
    name = 'Chuck Norris'

    def attack(self):
        self.use_weapon()
