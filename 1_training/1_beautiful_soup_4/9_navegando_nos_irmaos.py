from bs4 import BeautifulSoup

with open('arquivo02.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

print("*** soup.next_sibling ***\n\n", soup.next_sibling, '\n')

print("*** soup.td ***\n\n", soup.td, '\n')

print("*** soup.td.parent ***\n\n", soup.td.parent, '\n')

print("*** soup.td.next_sibling, acessa o espaço em branco ***\n\n", soup.td.next_sibling, '\n')

print("*** soup.td.next_sibling.next_sibling, acessa a próxima tag ***\n\n", soup.td.next_sibling.next_sibling, '\n')

print("*** iterando entre os próximos irmãos ***\n")
for siblings in soup.p.next_siblings:
    print(repr(siblings))
print('\n')

print("*** iterando entre os irmãos anteriores ***\n")
for siblings in soup.p.previous_siblings:
    print(repr(siblings))
print('\n')
