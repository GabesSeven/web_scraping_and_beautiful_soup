from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag

with open('arquivo02.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

print("*** imprimingo descendentes ***\n")
for tag in soup.descendants:
    if isinstance(tag, NavigableString):
        print(tag)
    else:
        print(tag.name)
print('\n')

print("*** imprimingo descendentes ***\n")
for tag in soup.descendants:
    if isinstance(tag, Tag):
        print(tag)
print('\n')

print("*** diferença entre strings e stripped_strings que remove espaços extras ***\n")
for string in soup.aside.strings:
    print(repr(string))
print('\n')

print("*** diferença entre strings e stripped_strings que remove espaços extras ***\n")
for string in soup.aside.stripped_strings:
    print(repr(string))
print('\n')