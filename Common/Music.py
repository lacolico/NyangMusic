import Common.EnumList as EL

class Music:
    def __init__(self, isrc: str, title: str, artist: str, **kwargs):
        self.__isrc = isrc                          # 국제 표준 ID
        self.__title = title                        # 제목
        self.__artist = artist                      # 아티스트
        self.__lricist = kwargs.get('lricist', '')   # 작사가
        self.__composer = kwargs.get('composer', '') # 작곡가
        self.__platform = kwargs.get('platform', EL.Platform.SOUNDCLOUD) # 다운로드 플랫폼

    # Getter ------------------------------
    @property
    def isrc(self):
        return self.__isrc

    @property
    def title(self):
        return self.__title

    @property
    def artist(self):
        return self.__artist

    @property
    def lricist(self):
        return self.__lricist

    @property
    def composer(self):
        return self.__composer

    @property
    def platform(self):
        return self.__platform

    # Setter ------------------------------
    @isrc.setter
    def isrc(self, isrc):
        self.__isrc = isrc

    @title.setter
    def title(self, title):
        self.__title = title

    @artist.setter
    def artist(self, artist):
        self.__artist = artist

    @lricist.setter
    def lricist(self, lricist):
        self.__lricist = lricist

    @composer.setter
    def composer(self, composer):
        self.__composer = composer

    @platform.setter
    def platform(self, platform):
        self.__platform = platform