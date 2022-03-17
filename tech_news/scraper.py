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
    selector = parsel.Selector(html_content)
    tec = selector.css('div.tec--list')
    link = tec.css('a.tec--btn::attr(href)').get()
    return link


# Requisito 4
def strip_string(text):
    return text.strip()


def format_counters(counter):
    if (not counter):
        return 0
    number = ''.join(filter(lambda char: char.isdigit(), counter))
    if (number == ''):
        return 0
    return int(number)


def format_array(array):
    result = map(strip_string, array)
    return list(result)


def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    article = selector.css('article.tec--article')
    title = article.css('h1.tec--article__header__title::text').get()
    timestamp = article.css('time::attr(datetime)').get()
    writer = article.css('.z--font-bold *::text').get()

    sources = article.css('div.z--mb-16 a.tec--badge::text').getall()
    categories = article.css('a.tec--badge--primary::text').getall()

    article_toolbar = selector.css('nav.tec--toolbar')
    shares_count = article_toolbar.css('div.tec--toolbar__item::text').get()
    comments_count = article_toolbar.css('button.tec--btn::text').get()

    article_body = selector.css('div.tec--article__body')
    summary_tag = article_body.css('p:first-child *::text').getall()
    summary = ''.join(summary_tag)

    url = selector.css('link[rel=canonical]::attr(href)').get()
    news = {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': strip_string(writer),
        'shares_count': format_counters(shares_count),
        'comments_count': format_counters(comments_count),
        'summary': summary,
        'sources': format_array(sources),
        'categories': format_array(categories)
    }
    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

