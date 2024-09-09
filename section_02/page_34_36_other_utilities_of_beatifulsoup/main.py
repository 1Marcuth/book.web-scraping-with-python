from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')

names = bs.find_all('span', { 'class': 'green' }) # 'bs.findAll' também funciona

"""
# Também funciona assim
.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
"""

# ----- Argumento: 'keyword' ------ #
"""
'.find_all(limit=1)' é equivalente a usar '.find()'
"""
# first_name = bs.find_all('span', { 'class': 'green' }, limit=1)
# first_name = bs.find('span', { 'class': 'green' })

# ----- Argumento: 'text' ------ #

# names = bs.find_all(text="the prince") # outra coisa
# print(len(names))

# ----- Argumento: 'keyword' ------ #

# title = bs.find_all(id='title', class_='text') >>> bs.find_all(id='title')
# print(title)

"""
# As duas linhas fazem a mesma coisa
bs.find_all(id='text')
bs.find_all('', { 'id': 'text' })
"""

for name in names:
    print(name.text) # 'name.get_text()' também funciona
