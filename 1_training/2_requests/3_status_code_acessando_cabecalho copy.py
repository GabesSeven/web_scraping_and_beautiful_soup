import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/"
# url = "https://www.google.com/404"

r= requests.get(url)

"""
Status code
"""
print(r.status_code)
if r.status_code == requests.codes.ok:
   #  print("Programa continua...")
   soup = BeautifulSoup(r.text, "html.parser")

"""
Headers
"""
# print(r.headers)
# print(r.headers["Set-Cookie"])
print(r.request.headers)