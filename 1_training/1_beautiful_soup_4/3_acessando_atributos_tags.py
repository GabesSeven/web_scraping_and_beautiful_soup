from bs4 import BeautifulSoup

with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

print("*** soup.p['class'] ***\n\n", soup.p['class'], '\n')

print("*** soup.p.attrs ***\n\n", soup.p.attrs, '\n')

print("*** soup.a['href'] ***\n\n", soup.a['href'], '\n')

print("*** soup.a.get('href'), retorna erro caso tag não exista ***\n\n", soup.a.get('href'), '\n')
