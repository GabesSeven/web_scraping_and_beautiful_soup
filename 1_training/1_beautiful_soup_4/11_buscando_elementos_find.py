'''
Buscando de cima pra baixo na estrutura de árvore. 
'''
from bs4 import BeautifulSoup

with open('arquivo04.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

tag = soup.find('li')
print("*** soup.find('li'), buscando por tag ***\n\n", tag, '\n')

tag = soup.find(string='plants')
print("*** soup.find(string='plants'), buscando por texto ***\n\n", tag, '\n')

tag = soup.find(id='secondaryconsumers')
print("*** soup.find(id='secondaryconsumers'), buscando por id ***\n\n", tag, '\n')

tag = soup.find(attrs={'class': 'primaryconsumerlist'})
print("*** soup.find(attrs={'class': 'primaryconsumerlist'}), buscando por classe CSS ***\n\n", tag, '\n')

tag = soup.find('ul', attrs={'class': 'producerlist'})
print("*** soup.find('ul', attrs={'class': 'producerlist'}), buscando com mais de um filtro ***\n\n", tag, '\n')

tag = soup.ul.li.find('li')
print("*** soup.ul.li.find('li'), buscando dentro de uma tag ***\n\n", tag, '\n')


print("*** função de verificação de tags ***\n")
def is_secondary_consumers(tag):
    return tag.has_attr('id') and tag.get('id') == 'secondaryconsumers'

secondary_consumers = soup.find(is_secondary_consumers)
print(secondary_consumers.li.div.string)