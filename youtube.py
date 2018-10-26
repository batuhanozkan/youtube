from __future__ import unicode_literals
import youtube_dl
import requests
from bs4 import BeautifulSoup

link="https://www.youtube.com/results?q="
indirilecek=input("Youtubeden şarkılarını indirmek istediğiniz şarkıcı seçin")
link=link+indirilecek
istek=requests.get(link)
icerik = BeautifulSoup(istek.content,"html.parser")
icerik=icerik.find_all('div',{"class" : "yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix"})
for x in icerik:
    d=str(x)
    d=d[94:107]
    print(d)
    try:
        ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }],
        }
        d=d[1:12]
        link="https://www.youtube.com/watch?v="
        link=link+d
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            
            #ydl.download([link])
               info = ydl.extract_info(link, download=True)
        songname = info.get('title', None)
        
    except (youtube_dl.utils.PostProcessingError,youtube_dl.utils.DownloadError):
        pass
