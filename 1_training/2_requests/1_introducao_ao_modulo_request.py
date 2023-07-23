import requests

url = "https://www.youtube.com/results?"
payload = {"search_query": "como fazer strogonoff de frango"}

r = requests.get(url, params=payload)
# print(r.text)
# print(r.url)
print(r.encoding)

with open('youtube.html', 'w') as f:
    f.write(r.text)

with open('youtube_2.html', 'wb') as f:
    f.write(r.content)