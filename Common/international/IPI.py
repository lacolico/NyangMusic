from typing import List
import enum


class IPIFormat(enum.Enum):
    SEP: str = "{header}-{id}-{check}"
    NO_SEP: str = "{header}{id}{check}"


class IPI:
    def __init__(self, header: str, identification_number: List[int], check_digit: int):
        self._header: str = header
        self._identification_number: List[int] = identification_number
        self._check_digit: int = check_digit

    def __str__(self):
        return self.format(IPIFormat.SEP)

    def format(self, f: IPIFormat) -> str:
        return f.value.format(
            header=self._header,
            id="".join(map(str, self._identification_number)),
            check=self._check_digit,
        )


if __name__ == '__main__':
    ex = IPI("I", [0, 0, 1, 0, 6, 8, 1, 3, 0], 6)
    print(ex)
