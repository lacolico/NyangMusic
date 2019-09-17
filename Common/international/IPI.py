from __future__ import annotations

from typing import List, Tuple

import enum
import re


class IPIFormat(enum.Enum):
    SEP: Tuple[str, re.Pattern] = (
        "{header}-{id}-{check}",
        re.compile(
            r"(?P<header>[a-zA-Z0-9])-(?P<id>[0-9]{9})-(?P<check>[0-9])")
    )
    NO_SEP: str = (
        "{header}{id}{check}",
        re.compile(
            r"(?P<header>[a-zA-Z0-9])(?P<id>[0-9]{9})(?P<check>[0-9])")
    )


class IPI:
    def __init__(self, header: str, identification: List[int], check: int):
        self._header: str = header
        self._identification: List[int] = identification
        self._check: int = check

    def __str__(self):
        return self.format(IPIFormat.NO_SEP)

    def format(self, f: IPIFormat) -> str:
        return f.value[0].format(
            header=self.header,
            id=self.identification,
            check=self._check,
        )

    @classmethod
    def parse(cls, raw: str, fmt: IPIFormat = IPIFormat.NO_SEP) -> IPI:
        d = fmt.value[1].search(raw).groupdict()
        return cls(d["header"], list(map(int, list(d["id"]))), int(d["check"]))

    @property
    def header(self) -> str:
        return self._header

    @property
    def identification(self) -> str:
        return "".join(map(str, self._identification))

    @property
    def check(self) -> int:
        return self._check


if __name__ == '__main__':
    tmp = IPI.parse("I0010681306")

    print(tmp)
    print(tmp.header)
    print(tmp.identification)
    print(tmp.check)
