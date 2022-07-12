from abc import ABC, abstractmethod


class ABCWeapons(ABC):
    """
    Абстрактный класс миксина оружия.
    """
    @abstractmethod
    def use_weapon(self):
        pass


class Gun(ABCWeapons):
    def use_weapon(self):
        print('PIU PIU')


class Lasers(ABCWeapons):
    def use_weapon(self):
        print('Wzzzuuuup!')


class MartialArts(ABCWeapons):
    def use_weapon(self):
        print('Bump')
