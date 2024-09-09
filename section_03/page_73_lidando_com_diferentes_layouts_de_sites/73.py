from bs4 import BeautifulSoup
import requests

class Content:
    def __init__(self, url, title, body) -> None:
        self.url = url
        self.title = title
        self.body = body

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(\n\t{self.title=}\n\t{self.body=}\n\t{self.url=}\n)"

def get_page(url: str) -> BeautifulSoup:
    response = requests.get(url, headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' })
    return BeautifulSoup(response.text, 'html.parser')

def scrape_new_york_times(url: str) -> Content:
    bs = get_page(url)
    title = bs.find('h1').text
    lines = bs.select('.StoryBodyCompanionColumn div p')
    body = '\n'.join([ line.text for line in lines ])
    return Content(url, title, body)

def scrape_bookings(url: str) -> Content:
    bs = get_page(url)
    title = bs.find('h1').text
    lines = bs.find('div', { 'class': 'post-body' })
    body = '\n'.join([ line.text for line in lines ])
    return Content(url, title, body)

url = 'https://www.brookings.edu/blog/techtank/2023/06/02/around-the-halls-what-should-the-regulation-of-generative-ai-look-like/'

content = scrape_bookings(url)

print(content)

url = 'https://www.nytimes.com/2023/06/16/us/police-doj-report-highlights-minneapolis.html'
content = scrape_new_york_times(url)

print(content)