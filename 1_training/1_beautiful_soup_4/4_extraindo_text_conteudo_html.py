from bs4 import BeautifulSoup

with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'html5lib')

print("*** soup.prettify() ***\n\n", soup.prettify(), '\n')

print("*** soup.get_text() ***\n\n", soup.get_text(), '\n')

print("*** soup.p.get_text() ***\n\n", soup.p.get_text(), '\n')

print("*** soup.p.string ***\n\n", soup.p.string, '\n')

print("*** soup.p.b.string ***\n\n", soup.p.b.string, '\n')
