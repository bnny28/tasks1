from heroes import Superman, ChuckNorris, ABCHero
from mass_medias import NewsPapers, Radio, ABCMedia
from places import Kostroma, Tokyo, SomePlanet, ABCPlace


def save_the_place(hero: ABCHero,
                   place: ABCPlace,
                   mass_media: ABCMedia):
    hero.find(place)
    hero.attack()
    if hero.is_superhero:
        hero.ultimate()
    mass_media.create_news(place, hero)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), NewsPapers())
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo(), NewsPapers())
    print('-' * 20)
    save_the_place(ChuckNorris(), SomePlanet(), Radio())
