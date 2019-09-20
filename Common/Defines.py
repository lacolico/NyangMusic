import enum


# Enums
class DownloadPfType(enum.Enum):
    SOUNDCLOUD = enum.auto()


class InfoPfType(enum.Enum):
    GENIE = enum.auto()
    MUSICBRAINZ = enum.auto()


class ChartType(enum.Enum):
    TOP200 = enum.auto()
    GENRE = enum.auto()
    MUSICHISTORY = enum.auto()
    MUSICVIDEO = enum.auto()


class NewestType(enum.Enum):
    SONG = enum.auto()
    ALBUM = enum.auto()


# Consts
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


class Pf:
    @classmethod
    def get_platform(cls, p_type: InfoPfType = None):
        if p_type is None:
            return Genie
        elif p_type is InfoPfType.Genie:
            return Genie
        elif p_type is InfoPfType.MUSICBRAINZ:
            return MusicBrainz


class Genie:
    URL = 'https://www.genie.co.kr'

    CHART = URL + '/chart'
    CHART_TOP200 = CHART + '/top200'
    CHART_GENRE = CHART + '/genre'
    CHART_MUSIC_HISTORY = CHART + '/musicHistory'
    CHART_MUSIC_VIDEO = CHART + '/musicVideo'

    NEWEST = URL + '/newest'
    NEWEST_SONG = NEWEST + '/song'
    NEWEST_ALBUM = NEWEST + '/album'

    @classmethod
    def get_url(cls):
        return cls.URL

    @classmethod
    def get_url_chart(cls, c_type: ChartType = None):
        if c_type is None:
            return cls.CHART
        elif c_type is ChartType.TOP200:
            return cls.CHART_TOP200
        elif c_type is ChartType.GENRE:
            return cls.CHART_GENRE
        elif c_type is ChartType.MUSIC_HISTORY:
            return cls.CHART_MUSIC_HISTORY
        elif c_type is ChartType.MUSIC_VIDEO:
            return cls.CHART_MUSIC_VIDEO

    @classmethod
    def get_url_newest(cls, n_type: NewestType = None):
        if n_type is None:
            return cls.NEWEST
        elif n_type is NewestType.SONG:
            return cls.NEWEST_SONG
        elif n_type is NewestType.ALBUM:
            return cls.NEWEST_ALBUM


class MusicBrainz:
    URL = ''


class SoundCloud:
    URL = ''

