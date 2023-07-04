from bs4 import BeautifulSoup

with open('arquivo02.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

print("*** soup.parent ***\n\n", soup.parent, '\n')

tag_title = soup.title
print("*** soup.title ***\n\n", tag_title, '\n')

print("*** soup.title.parent ***\n\n", tag_title.parent, '\n')

print("*** soup.td.parent ***\n\n", soup.td.parent, '\n')

print("*** soup.td.parent.parent ***\n\n", soup.td.parent.parent, '\n')

print("*** iterando os pais ***\n")
for pai in soup.p.parents:
    print(pai.name)
print('\n')

