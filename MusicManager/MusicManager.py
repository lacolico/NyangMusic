import soundcloud

clientID = '0b84ba9d7d0084c784c5a6533160ea39'
client = soundcloud.Client(client_id=clientID)

tSize = 20
tSearch = '너랑나'
tracks = client.get('/tracks', q=tSearch, limit=tSize)
for track in tracks:
    print(track.id)
    print(track.title)
track2 = client.get('/tracks/235177148')
print(track2.title)