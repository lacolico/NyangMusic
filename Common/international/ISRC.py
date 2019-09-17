import enum
from typing import List

import pycountry


class ISRCFormat(enum.Enum):
    SEP: str = "{country}-{registrant}-{year}-{designation}"
    NO_SEP: str = "{country}{registrant}{year}{designation}"


class ISRC:
    def __init__(self, country, registrant: str, year: int, designation: List[int]):
        self._country = country
        self._registrant: str = registrant
        self._year: int = year
        self._designation: List[int] = designation

    def __str__(self):
        return self.format(ISRCFormat.SEP)

    def format(self, f: ISRCFormat) -> str:
        return f.value.format(
            country=self._country,
            registrant=self._registrant,
            year=self._year,
            designation="".join(map(str, self._designation)),
        )

if __name__ == '__main__':
    tmp = pycountry.countries.get(alpha_2="KR")
    print(type(tmp))
    help(tmp)
    print(tmp)