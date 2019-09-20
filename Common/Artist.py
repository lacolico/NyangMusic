from Common.international import IPI
from typing import Dict, Any
import enum
import datetime


class Gender(enum.Enum):
    Male = enum.auto()
    Female = enum.auto()


class ArtistType(enum.Enum):
    Person = enum.auto()
    Group = enum.auto()


class Artist:
    def __init__(self,
                 ipi: IPI,
                 name: str = "",
                 artist_type: ArtistType = None,
                 gender: Gender = None,
                 country=None,
                 birth: datetime.date = None,
                 death: datetime.date = None,
                 **kwargs
                 ):
        self._ipi: IPI = ipi
        self._name = name
        self._artist_type = artist_type
        self._gender = gender
        self._country = country
        self._birth = birth
        self._death = death

        self._metadata = kwargs

    def is_valid(self) -> bool:
        return self._ipi is not None

    @property
    def name(self) -> str:
        return self._name

    @property
    def country(self):
        return self._country

    @property
    def country_code2(self) -> str:
        if self._country is not None:
            return self._country.alpha_2
        return ""

    @property
    def gender(self) -> Gender:
        return self._gender

    @property
    def artist_type(self) -> ArtistType:
        return self._artist_type

    @property
    def birth(self) -> datetime.date:
        return self._birth

    @property
    def death(self) -> datetime.date:
        return self._death

    @property
    def metadata(self) -> Dict[str, Any]:
        return self._metadata
