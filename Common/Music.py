from Common import Defines


class Music:
    def __init__(self, isrc: str, title: str, artist: str, **kwargs):
        self._isrc = isrc  # 국제 표준 ID
        self._title = title  # 제목
        self._artist = artist  # 아티스트
        self._lricist = kwargs.get('lricist', '')  # 작사가
        self._composer = kwargs.get('composer', '')  # 작곡가
        self._platform = kwargs.get('platform', Defines.Platform.SOUND_CLOUD)  # 다운로드 플랫폼

    # Getter ------------------------------
    @property
    def isrc(self) -> str:
        return self._isrc

    @property
    def title(self) -> str:
        return self._title

    @property
    def artist(self) -> str:
        return self._artist

    @property
    def lricist(self) -> str:
        return self._lricist

    @property
    def composer(self) -> str:
        return self._composer

    @property
    def platform(self) -> str:
        return self._platform

    # Setter ------------------------------
    @isrc.setter
    def isrc(self, isrc: str):
        self._isrc = isrc

    @title.setter
    def title(self, title: str):
        self._title = title

    @artist.setter
    def artist(self, artist: str):
        self._artist = artist

    @lricist.setter
    def lricist(self, lricist: str):
        self._lricist = lricist

    @composer.setter
    def composer(self, composer: str):
        self._composer = composer

    @platform.setter
    def platform(self, platform: str):
        self._platform = platform
