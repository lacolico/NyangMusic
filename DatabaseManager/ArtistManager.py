import enum
from typing import List, Callable, Dict
from Common import Artist
import musicbrainzngs
import pycountry
import datetime

musicbrainzngs.set_useragent("NyangMusic", "0.0.1")


class QueryEntity(enum.Enum):
    Artist = enum.auto()
    Track = enum.auto()
    Record = enum.auto()


class ExternalDatabase:
    def __init__(self, *args, **kwargs):
        pass

    def query_artist(self, query: str, selector: Callable[[Artist.Artist], bool],
                     country=None,
                     qtype: str = None) -> List[Artist.Artist]:
        return None


class Musicbrainz(ExternalDatabase):

    @staticmethod
    def parse_artist_type(arg: str) -> Artist.ArtistType:
        if arg is None:
            return None
        if arg == "Person":
            return Artist.ArtistType.Person
        if arg == "Group":
            return Artist.ArtistType.Group
        return None

    @staticmethod
    def parse_gender(arg: str) -> Artist.Gender:
        if arg is None:
            return None
        if arg == "female":
            return Artist.Gender.Female
        if arg == "male":
            return Artist.Gender.Male
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

    def query_artist(self, query: str, selector: Callable[[Artist.Artist], bool],
                     country=None,
                     qtype: str = None) -> List[Artist.Artist]:
        field = {}
        if country is not None:
            field['country'] = country.alpha_2
        if qtype is not None:
            field['type'] = qtype
        # search fields
        result = filter(
            selector,
            map(
                lambda artist: Artist.Artist(
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


class ArtistManager:
    def __init__(self, extdb: ExternalDatabase):
        self._extdb = extdb

    def search(self, query: str) -> List[Artist.Artist]:
        return []


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
