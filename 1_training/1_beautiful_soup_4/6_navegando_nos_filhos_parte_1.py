from bs4 import BeautifulSoup

with open('arquivo02.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

print("*** soup.table.contents ***\n\n", soup.table.contents, '\n')

print("*** type(soup.table.contents) ***\n\n", type(soup.table.contents), '\n')

print("*** len(soup.table.contents) ***\n\n", len(soup.table.contents), '\n')

print("*** soup.table.contents[1] ***\n\n", soup.table.contents[1], '\n')

print("*** soup.table.contents[1].span ***\n\n", soup.table.contents[1].span, '\n')

print("*** soup.table.contents[3].td ***\n\n", soup.table.contents[3].td, '\n')

print("*** soup.tr ***\n\n", soup.tr, '\n')

print("*** soup.tr.td ***\n\n", soup.tr.td, '\n')

print("*** soup.td.attrs ***\n\n", soup.td.attrs, '\n')

print("*** soup.td['class'] ***\n\n", soup.td['class'], '\n')

print("*** soup.td['class'][0] ***\n\n", soup.td['class'][0], '\n')

print("*** imprimingo filhos ***\n")
for child in soup.table.contents:
    print(child)
print('\n')


print("*** imprimingo filhos ***\n")
for child in soup.table.contents:
    if child.name == 'tr':
        print(child)
print('\n')

print("*** type(soup.children) ***\n\n", type(soup.children), '\n')

print("*** imprimingo filhos ***\n")
for child in soup.footer.children:
    print(child)
print('\n')

print("*** imprimingo filhos ***\n")
for child in soup.footer.p.children:
    if child.name == 'a':
        print(child.get('href'))
print('\n')

print("*** len(list(soup.children)) ***\n\n", len(list(soup.children)), '\n')

print("*** len(list(soup.descendants)) ***\n\n", len(list(soup.descendants)), '\n')
