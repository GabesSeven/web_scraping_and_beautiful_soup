'''
Buscando de baixo pra cima na estrutura de árvore. 
'''
from bs4 import BeautifulSoup

with open('arquivo04.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

primaryconsumers = soup.find_all(class_='primaryconsumerlist')
primaryconsumer = primaryconsumers[0]
print("*** soup.find_all(class_='primaryconsumerlist')[0], ***\n\n", primaryconsumer, '\n')

parent_ul = primaryconsumer.find_parents('ul')
print("*** soup.find_all(class_='primaryconsumerlist')[0].find_parents('ul') ***\n\n", parent_ul, '\n')

parent_ul = primaryconsumer.find_parent('ul')
print("*** soup.find_all(class_='primaryconsumerlist')[0].find_parent('ul') ***\n\n", parent_ul, '\n')
