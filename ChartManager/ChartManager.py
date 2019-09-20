import requests
from Common import Defines
from bs4 import BeautifulSoup

url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20190917&hh=22&rtm=Y&pg=1'
resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div.music-list-wrap > table.list-wrap > tbody > tr.list')

for song in songs:
    title = song.find('td', {'class': 'info'}).find('a', {'class': 'title ellipsis'}).text.strip()
    print(title)

class ChartManager:
    def __init__(self, platform: Defines.PlatformType):
        self._platform = platform

    @classmethod
    def get_chart_list(cls, page: int, c_type: Defines.ChartType):
        headers = Defines.HEADERS
        url =


if __name__ == '__main__':
    ChartManager.getChart(1)