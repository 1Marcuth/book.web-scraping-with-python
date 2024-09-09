from turtle import title
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Conectando-se de forma confiável e tratando exeções

def get_title(url):
    try:
        html = urlopen(url)

    except HTTPError as e:
        print(e)

        # Devolve 'null', executa um 'break' ou algum outro "Plano B"

    except URLError as e:
        print('The server could not be found!')

    else:
        # O programa continua. Nota: se você retornar um 'break' no 'except' da exeção, não será necessário usar a instrução 'else'
        print('It Worked!')
        
        bs = BeautifulSoup(html, "html.parser")

        # Tratando erro de conteúdo de tag

        try:
            title = bs.body.h1
        
        except AttributeError as e:
            return None

        else:
            return title

title = get_title('http://pythonscraping.com/pages/page1.html')

if title == None:
    print('Title could not be found')

else:
    print(title)