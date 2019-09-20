from platform import ChartType, NewestType, Platform



class Genie(Platform):
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
