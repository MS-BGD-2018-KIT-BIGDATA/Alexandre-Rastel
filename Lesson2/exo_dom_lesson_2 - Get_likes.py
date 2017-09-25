import requests

url = "https://www.googleapis.com/youtube/v3/videos"

payload = { 'id': 'o1oyVvp-Tf8',#'7lCDEYXw3mM',
            'key':'AIzaSyDvdlISuEqFVm4s_0bP5vHpmJlPnocCHE0',
            'part':'snippet,contentDetails,statistics,status'}

r = requests.get(url, params=payload)
res = dict(r.json())

stats = res['items'][0]['statistics']

print(stats)
