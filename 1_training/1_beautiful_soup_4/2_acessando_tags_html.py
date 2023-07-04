from bs4 import BeautifulSoup

with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

tag = soup.title
print('*** soup.title ***\n\n', tag, '\n')

print('*** soup.title.name ***\n\n', tag.name, '\n')

print('*** soup.p ***\n\n', soup.p, '\n')

