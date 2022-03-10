import requests
import parsel
import time


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except requests.HTTPError:
        return None
    except requests.ReadTimeout:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    news = []
    if html_content == '':
        return news
    selector = parsel.Selector(html_content)
    for tec in selector.css('div.tec--list'):
        links = tec.css('a.tec--card__title__link::attr(href)').getall()
    news = links
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


html = fetch('https://www.tecmundo.com.br/novidades')
scrape_novidades(html)
