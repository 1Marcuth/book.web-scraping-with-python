from urllib.request import urlopen
from bs4 import BeautifulSoup

# Executando o BeatifulSoup

"""
- BeautifulSoup

    - Pode ser passado a string 'html.read()' ou o o bjeto _UrlopenRet 'html'

- A tag 'h1' do documento pode ser buscado com:
    - bs.html.body.h1
    - bs.html.h1
    - bs.body.h1
    - bs.h1

- Bibliotecas de parse de HTML:
    - lxml
    - html5lib

"""

html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html, 'html.parser')
print(bs.h1)