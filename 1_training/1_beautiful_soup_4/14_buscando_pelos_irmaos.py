'''
Buscando mesma hierarquia na estrutura de árvore. 
'''
from bs4 import BeautifulSoup

with open('arquivo03.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

producers = soup.find(id='producers')
next_sibling = producers.find_next_sibling()
print("*** soup.find(id='producers').find_next_sibling(), ***\n\n", next_sibling, '\n')

producers = soup.find(id='producers')
next_siblings = producers.find_next_siblings()
print("*** soup.find(id='producers').find_next_siblings(), ***\n\n", next_siblings, '\n')

producers = soup.find(id='quaternaryconsumers')
previous_sibling = producers.find_previous_sibling()
print("*** soup.find(id='quaternaryconsumers').find_previous_sibling(), ***\n\n", previous_sibling, '\n')

producers = soup.find(id='quaternaryconsumers')
previous_siblings = producers.find_previous_siblings()
print("*** soup.find(id='quaternaryconsumers').find_previous_siblings(), ***\n\n", previous_siblings, '\n')
