import requests
r = requests.get('http://google.com', timeout=0.03)
r = requests.get('http://google.com', timeout=None)
r = requests.get('http://google.com', timeout=(3.05, 27))

