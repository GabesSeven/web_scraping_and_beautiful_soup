'''
Buscando de cima pra baixo na estrutura de árvore. 
'''
from bs4 import BeautifulSoup

with open('arquivo03.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

tag_list = soup.find_all('ul')
print("*** soup.find_all('ul'), buscando por tag ***\n\n", tag_list, '\n')


tag_list = soup.find_all(['ul', 'div'])
print("*** soup.find_all(['ul', 'div']), buscando por lista de tags ***\n\n", tag_list, '\n')

tag_list = soup.find_all('ul', limit=2)
print("*** soup.find_all('ul', limit=2), buscando por tag, mas limitando quantidade de resultados ***\n\n", tag_list, '\n')

tag_list = soup.find_all(string='rabbit')
print("*** soup.find_all(string='rabbit'), buscando por string ***\n\n", tag_list, '\n')

tag_list = soup.find_all(string=True)
print("*** soup.find_all(string=True), buscando todos os textos ***\n\n", tag_list, '\n')

tag_list = soup.find_all(string=['rabbit', 'bear'])
print("*** soup.find_all(string=['rabbit', 'bear']), buscando lista de strings ***\n\n", tag_list, '\n')


tag_list = soup.find_all(class_=['producerlist', 'primaryconsumerlist'])
print("*** soup.find_all(class_=['producerlist', 'primaryconsumerlist']), buscando lista de classes ***\n\n", tag_list, '\n')

tag_list = soup.ul.find_all('div')
print("*** soup.ul.find_all('div'), buscando a partir de uma tag ***\n\n", tag_list, '\n')

tag_list = soup.ul.find_all('div', class_='name')
print("*** soup.ul.find_all('div', class_='name'), buscando com mais de um argumento ***\n\n", tag_list, '\n')