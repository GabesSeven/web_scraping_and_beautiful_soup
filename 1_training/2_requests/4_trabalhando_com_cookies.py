import requests

url = 'https://www.submarino.com.br'

r = requests.get(url)
cookie = r.cookies.get_dict()

busca = 'notebook'
url = 'http://busca.submarino.com.br/busca.php?={0}'.format(busca)

r = requests.get(url, cookies=cookie)

