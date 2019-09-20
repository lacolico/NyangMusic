import enum

from .genie import *
from .musicbrainz import *
from .platform import *
from .soundcloud import *


class NewestType(enum.Enum):
    SONG = enum.auto()
    ALBUM = enum.auto()


class ChartType(enum.Enum):
    TOP200 = enum.auto()
    GENRE = enum.auto()
    MUSICHISTORY = enum.auto()
    MUSICVIDEO = enum.auto()


class QueryEntity(enum.Enum):
    Artist = enum.auto()
    Track = enum.auto()
    Record = enum.auto()

# import soundcloud
#
# clientID = '0b84ba9d7d0084c784c5a6533160ea39'
# client = soundcloud.Client(client_id=clientID)
#
# tSize = 20
# tSearch = '너랑나'
# tracks = client.get('/tracks', q=tSearch, limit=tSize)
# for track in tracks:
#     print(track.id)
#     print(track.title)
# track2 = client.get('/tracks/235177148')
# print(track2.title)

# import requests
# from common import defines
# from bs4 import BeautifulSoup
#
# url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20190917&hh=22&rtm=Y&pg=1'
# # resp = requests.get(url, headers=headers)
# soup = BeautifulSoup(resp.text, 'html.parser')
#
# songs = soup.select('#body-content > div.newest-list > div.music-list-wrap > table.list-wrap > tbody > tr.list')
#
# for song in songs:
#     title = song.find('td', {'class': 'info'}).find('a', {'class': 'title ellipsis'}).text.strip()
#     print(title)
#
# class ChartManager:
#     def __init__(self, platform: defines.PlatformType):
#         self._platform = platform
#
#     @classmethod
#     def get_chart_list(cls, page: int, c_type: defines.ChartType):
#         headers = defines.HEADERS
#         url =
#
#
# if __name__ == '__main__':
#     ChartManager.getChart(1)
