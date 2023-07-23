import requests

url = 'http://google.com/'

try:
    r = requests.get(url, timeout=0.03)
except requests.exceptions.ConnectionError as e:
	print('ConnectionError')
except requests.exceptions.HTTPError as e:
	print ('HTTPError')
except requests.exceptions.Timeout as e:
	print ('Timeout')
except requests.exceptions.TooManyRedirects as e:
	print ('TooManyRedirects')
except requests.exceptions.RequestException as e:
	print ('RequestException')