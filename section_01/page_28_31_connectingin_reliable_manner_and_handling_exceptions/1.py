from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Conectando-se de forma confiável e tratando exeções

try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')

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
        bad_content = bs.non_existent_tag.another_tag
    
    except AttributeError as e:
        print('Tag was not found')

    else:
        if bad_content == None:
            print('Tag was not found')

        else:
            print(bad_content)
