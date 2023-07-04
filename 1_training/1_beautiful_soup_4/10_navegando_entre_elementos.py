from bs4 import BeautifulSoup
from bs4.element import Tag

with open('arquivo03.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

print("*** soup.div.next_element ***\n\n", soup.div.next_element, '\n')

print("*** soup.div.next_element.next_element ***\n\n", soup.div.next_element.next_element, '\n')

print("*** soup.div.next_element.next_element.next_element ***\n\n", soup.div.next_element.next_element.next_element, '\n')

print("*** soup.div.next_element.next_element.next_element.next_element ***\n\n", soup.div.next_element.next_element.next_element.next_element, '\n')

print("*** soup.div.previous_element.previous_element ***\n\n", soup.div.previous_element.previous_element, '\n')

print("*** iterando entre os elementos ***\n")
for e in soup.ul.next_elements:
    if isinstance(e, Tag): 
        print(e)
print('\n')

print("*** iterando entre os elementos ***\n")
for e in soup.li.previous_elements:
    print(repr(e))
print('\n')