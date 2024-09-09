from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def get_links(page_url: str):
    html = urlopen(f'http://en.wikipedia.org{page_url}')
    bs = BeautifulSoup(html, 'html.parser')

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        new_page = link.attrs['href']
        print(new_page)
        pages.add(new_page)
        get_links(new_page)

get_links('')
