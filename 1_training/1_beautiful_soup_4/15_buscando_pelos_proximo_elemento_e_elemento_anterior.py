'''
Buscando não respeitando hierarquia de elementos na estrutura de árvore. 
'''
from bs4 import BeautifulSoup

with open('arquivo03.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

producers = soup.find(id='producers')
tag_next = producers.find_next()
print("*** soup.find(id='producers').find_next(), ***\n\n", tag_next, '\n')

producers = soup.find(id='producers')
tags_next = producers.find_all_next()
print("*** soup.find(id='producers').find_all_next(), ***\n\n", tags_next, '\n')

producers = soup.find(id='quaternaryconsumers')
tag_previous = producers.find_previous()
print("*** soup.find(id='quaternaryconsumers').find_previous(), ***\n\n", tag_previous, '\n')

producers = soup.find(id='quaternaryconsumers')
tags_previous = producers.find_all_previous()
print("*** soup.find(id='quaternaryconsumers').find_all_previous(), ***\n\n", tags_next, '\n')
