import requests

r = requests.get('http://google.com')

print(r.url)
print(r.status_code)
print(r.history)
print(r.history[0].status_code)
print(r.history[0].headers)
print(r.history[0].headers['Location'])

r = requests.get('http://google.com', allow_redirects=False)

print(r.url)
print(r.history)