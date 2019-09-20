from typing import Callable, List

from common import artist


class Platform:
    def __init__(self, *args, **kwargs):
        pass

    def query_artist(self, query: str, selector: Callable[[artist.Artist], bool],
                     country=None,
                     qtype: str = None) -> List[artist.Artist]:
        return None