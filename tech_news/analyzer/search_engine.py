from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news = []
    news_found = []

    news_found = search_news({
        'title': {'$regex': title, '$options': 'i'}
    })
    news = list(map(lambda news: (news['title'], news['url']), news_found))
    return news


# Requisito 7
def search_by_date(date):
    try:
        date_format = '%Y-%m-%d'
        datetime.strptime(date, date_format)
        news = []
        news_found = []

        news_found = search_news({
            'timestamp': {'$regex': date}
        })
        news = list(map(lambda news: (news['title'], news['url']), news_found))
        print(news)
        return news
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
