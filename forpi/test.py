import requests
import json 
import urllib.request 
res = requests.get('http://localhost:9999/get-image')
url = res.json()['image']
print(url)
urllib.request.urlretrieve(url, "image.png") 