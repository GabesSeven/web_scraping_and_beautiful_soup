from bs4 import BeautifulSoup

with open('arquivo02.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

print("*** soup.title ***\n\n", soup.title, '\n')

print("*** soup.head.title ***\n\n", soup.head.title, '\n')

print("*** soup.a ***\n\n", soup.a, '\n')

print("*** soup.a.img ***\n\n", soup.a.img, '\n')

print("*** soup.td ***\n\n", soup.td, '\n')

print("*** soup.tr ***\n\n", soup.tr, '\n')

print("*** soup.tr.td ***\n\n", soup.tr.td, '\n')

print("*** soup.td.attrs ***\n\n", soup.td.attrs, '\n')

print("*** soup.td['class'] ***\n\n", soup.td['class'], '\n')

print("*** soup.td['class'][0] ***\n\n", soup.td['class'][0], '\n')

