from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import random
import time
import re

random.seed(time.time())

pages = set()

# Obtém uma lista de todos os links internos encontrados em uma página
def get_internal_links(bs: BeautifulSoup, include_url) -> list[str]:
    include_url = "{}://{}".format(
        urlparse(include_url).scheme,
        urlparse(include_url).netloc
    )

    internal_links = []
    
    # Encontra todos os links que começam com "/"

    for link in bs.find_all(
        "a",
        href=re.compile("^(\|.*" + include_url + ")")
    ):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in internal_links:
                if (link.attrs["href"].startswith("/")):
                    internal_links.append(link.attrs["href"])

    return internal_links

# Obtém uma lista de todos os links externos encontrados em uma página 
def get_external_links(bs: BeautifulSoup, exclude_url: str) -> list[str]:
    external_links = []

    # Encontra todos os links qye cineçam com "http" e que não contenham a url atual;

    for link in bs.find_all("a", href="^(http|www)((?!" + exclude_url + "))"):
        if link["attrs"]["href"] is not None:
            if link.attrs["href"] not in external_links:
                external_links.append(link.attrs["href"])

    return external_links

def get_random_external_link(starting_page: str) -> str:
    html = urlopen(starting_page)
    bs = BeautifulSoup(html, "html.parser")

    external_links = get_external_links(
        bs, urlparse(starting_page).scheme
    )

    if len(external_links) == 0:
        print("No external links, loking around the site for one")

        domin = "{}:{}".format(
            urlparse(starting_page).scheme,
            urlparse(starting_page).netloc
        )

        internal_links = get_internal_links(bs, domin)

        return get_random_external_link(
            internal_links[random.randint(
                0,
                len(internal_links) - 1
            )]
        )
    
    else:
        return external_links[random.randint(
            0,
            len(external_links) - 1
        )]

def follow_exernal_only(starting_site) -> None:
    external_link = get_random_external_link(starting_site)

    print(f"Random external link is: {external_link}")

    follow_exernal_only(external_link)

follow_exernal_only("http://oreilly.com")