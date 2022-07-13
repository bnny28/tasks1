from abc import ABC, abstractmethod

from antagonists import Orcs, Godzilla, Aliens


class ABCPlace(ABC):
    """
    Абстрактный класс места нападения.
    """
    @abstractmethod
    def get_antagonist(self):
        pass

    def is_planet(self):
        return isinstance(self, ABCPlanet)


class ABCPlanet(ABCPlace):
    """
    Абстрактный класс планеты с координатами.
    """
    @property
    @abstractmethod
    def coordinates(self) -> [float]:
        pass


class ABCCity(ABCPlace):
    """
    Абстрактный класс города с именем.
    """
    @property
    @abstractmethod
    def name(self) -> str:
        pass


class Kostroma(ABCCity, Orcs):
    name = 'Kostroma'

    def get_antagonist(self):
        self.location_antagonist()


class Tokyo(ABCCity, Godzilla):
    name = 'Tokyo'

    def get_antagonist(self):
        self.location_antagonist()


class SomePlanet(ABCPlanet, Aliens):
    @property
    def coordinates(self) -> [float]:
        return [4.5, 6.8]

    def get_antagonist(self):
        self.location_antagonist()
