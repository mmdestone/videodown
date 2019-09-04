
import requests

 

print("开始下载")

url = 'https://video-qn.ibaotu.com/00/51/34/887888piCZM2.mp4'

r = requests.get(url,stream=True)

 

with open('G:/download/test.mp4', "wb") as mp4:

    for chunk in r.iter_content(chunk_size=1024 * 1024):

        if chunk:

            mp4.write(chunk)

 

print("下载结束")

 

 

