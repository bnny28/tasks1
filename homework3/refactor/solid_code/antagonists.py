from abc import ABC, abstractmethod


class ABCAntagonist(ABC):
    """
    Абстрактный класс миксина врага.
    """
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def location_antagonist(self):
        pass


class Orcs(ABCAntagonist):
    name = 'Orcs'

    def location_antagonist(self):
        print('Orcs hid in the forest')


class Godzilla(ABCAntagonist):
    name = 'Godzilla'

    def location_antagonist(self):
        print('Godzilla stands near a skyscraper')


class Aliens(ABCAntagonist):
    name = 'Aliens'

    def location_antagonist(self):
        print('Aliens have invaded the planet')
