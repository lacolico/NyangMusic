from __future__ import annotations

from typing import List, Tuple

import re
import enum
import pycountry


class ISRCFormat(enum.Enum):
    SEP: Tuple[str, re.Pattern] = (
        "{country}-{registrant}-{year}-{designation}",
        re.compile(
            r"(?P<country>[a-zA-Z]{2})-(?P<registrant>[a-zA-Z0-9]{3})-(?P<year>[0-9]{2})-(?P<designation>[0-9]{5})"),
    )
    NO_SEP: Tuple[str, re.Pattern] = (
        "{country}{registrant}{year}{designation}",
        re.compile(
            r"(?P<country>[a-zA-Z]{2})(?P<registrant>[a-zA-Z0-9]{3})(?P<year>[0-9]{2})(?P<designation>[0-9]{5})"),
    )


class ISRC:
    def __init__(self, country, registrant: str, year: int, designation: List[int]):
        self._country = country
        self._registrant: str = registrant
        self._year: int = year
        self._designation: List[int] = designation

    def __str__(self):
        return self.format(ISRCFormat.NO_SEP)

    def format(self, f: ISRCFormat) -> str:
        return f.value[0].format(
            country=self._country.alpha_2,
            registrant=self._registrant,
            year="{:02d}".format(self._year),
            designation=self.designation,
        )

    @classmethod
    def parse(cls, raw: str, fmt: ISRCFormat = ISRCFormat.NO_SEP) -> ISRC:
        d = fmt.value[1].search(raw).groupdict()
        return cls(pycountry.countries.get(alpha_2=d["country"]), d["registrant"], int(d["year"]),
                   list(map(int, list(d["designation"]))))

    @property
    def country(self):
        return self._country

    @property
    def registrant(self) -> str:
        return self._registrant

    @property
    def year(self) -> int:
        return self._year

    @property
    def designation(self) -> str:
        return "".join(map(str, self._designation))


if __name__ == '__main__':
    res = ISRC.parse("KRA381002339")
    print(res)
    print(res.country)
    print(res.registrant)
    print(res.year)
    print(res.designation)
