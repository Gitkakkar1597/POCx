import json
from newsplease import NewsPlease

# List of news website URLs to scrape
news_urls = [
    "https://www.cnn.com",
    "https://www.theguardian.com",
    "https://www.nytimes.com"
]

def scrape_news(urls):
    articles_data = []

    for url in urls:
        article = NewsPlease.from_url(url)
        if article:
            article_info = {
                "title": article.title,
                "text": article.text,
                "url": url,
                "authors": article.authors,
                "language": article.language,
            }
            articles_data.append(article_info)

    return articles_data

news_articles = scrape_news(news_urls)

print(json.dumps(news_articles, indent=4))
 