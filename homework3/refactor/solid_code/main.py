from typing import Union

from heroes import Superman, ChuckNorris, ABCSuperHero
from mass_medias import NewsPapers
from places import Kostroma, Tokyo, SomePlanet


def save_the_place(hero: Union[Superman, ChuckNorris],
                   place: Union[Kostroma, Tokyo, SomePlanet],
                   mass_media: NewsPapers):
    hero.find(place)
    hero.attack()
    if isinstance(hero, ABCSuperHero):
        hero.ultimate()
    mass_media.create_news(place, hero)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), NewsPapers())
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo(), NewsPapers())
    print('-' * 20)
    save_the_place(ChuckNorris(), SomePlanet(), NewsPapers())
