import datetime
from typing import List, Callable

import musicbrainzngs
import pycountry

from common import artist
from platform import Platform

musicbrainzngs.set_useragent("NyangMusic", "0.0.1")


class Musicbrainz(Platform):

    @staticmethod
    def parse_artist_type(arg: str) -> artist.ArtistType:
        if arg is None:
            return None
        if arg == "Person":
            return artist.ArtistType.Person
        if arg == "Group":
            return artist.ArtistType.Group
        return None

    @staticmethod
    def parse_gender(arg: str) -> artist.Gender:
        if arg is None:
            return None
        if arg == "female":
            return artist.Gender.Female
        if arg == "male":
            return artist.Gender.Male
        return None

    @staticmethod
    def parse_country(arg: str):
        if arg is None:
            return None
        return pycountry.countries.get(alpha_2=arg)

    @staticmethod
    def parse_birth(arg: str):
        if arg is None:
            return None
        return datetime.datetime.strptime(arg, "%Y-%m-%d").date()

    @staticmethod
    def parse_death(arg: str):
        if arg is None:
            return None
        if arg is 'false':
            return None
        if arg is 'true':
            return None
        return datetime.datetime.strptime(arg, "%Y-%m-%d").date()

    def query_artist(self, query: str, selector: Callable[[artist.Artist], bool],
                     country=None,
                     qtype: str = None) -> List[artist.Artist]:
        field = {}
        if country is not None:
            field['country'] = country.alpha_2
        if qtype is not None:
            field['type'] = qtype
        # search fields
        result = filter(
            selector,
            map(
                lambda artist: artist.Artist(
                    None,
                    name=artist.get("name", ""),
                    artist_type=Musicbrainz.parse_artist_type(artist.get("type")),
                    gender=Musicbrainz.parse_gender(artist.get("gender")),
                    country=Musicbrainz.parse_country(artist.get("country")),
                    birth=Musicbrainz.parse_birth(artist.get("life-span", {}).get("begin")),
                    death=Musicbrainz.parse_death(artist.get("life-span", {}).get("end")),
                    mbid=artist.get("id"),
                ),
                musicbrainzngs.search_artists(query, **field)['artist-list']
            )
        )
        # more infomation searching
        return list(result)


if __name__ == '__main__':
    m = Musicbrainz()
    for a in m.query_artist("IU", lambda a: a.country_code2 == "KR"):
        print(a.is_valid())
        print(a.name)
        print(a.artist_type)
        print(a.gender)
        print(a.country)
        print(a.country_code2)
        print(a.birth)
        print(a.death)
        print(a.metadata)
        print()
