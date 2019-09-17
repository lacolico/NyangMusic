import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20190917&hh=22&rtm=Y&pg=1'
resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div.music-list-wrap > table.list-wrap > tbody > tr.list')
for song in songs:
    title = song.find('td', {'class':'info'}).find('a', {'class':'title ellipsis'}).text.strip()
    print(title)