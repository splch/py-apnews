import requests
from bs4 import BeautifulSoup
import time

base_url = "https://apnews.com"
top_news_url = base_url + "/hub/ap-top-news"

def get_url(url, sleep=1):
    time.sleep(sleep)
    return requests.get(url)

def parse_top_news(response):
    news = []
    # If the GET request is successful, the status code will be 200
    if response.status_code == 200:
        # Get the content of the response
        webpage = response.content
        # Create a BeautifulSoup object and specify the parser
        soup = BeautifulSoup(webpage, "html.parser")
        # Find all the articles on the page
        articles = soup.find_all("div", {"class": "FeedCard"})
        # For each article, find the headline and the link
        for article in articles:
            headlines = map(lambda h2: h2.text, article.find_all("h2"))
            links = map(lambda a: a["href"], article.find_all("a"))
            for headline, link in zip(headlines, links):
                news.append((headline, base_url + link))
    return news

def parse_article(response):
    # If the GET request is successful, the status code will be 200
    if response.status_code == 200:
        # Get the content of the response
        webpage = response.content
        # Create a BeautifulSoup object and specify the parser
        soup = BeautifulSoup(webpage, "html.parser")
        # Parse the article title and body
        title = soup.find("h1").text
        body = soup.find("div", {"class": "Article"})
        # Return title and body
        return title, body.text

def get_top_articles(news, n=5):
    _news = []
    for headline, url in news[:n]:
        article = get_url(url)
        _news.append(parse_article(article))
    return _news

def scrape_top_news():
    # Send a GET request to the website
    top_news = get_url(top_news_url, sleep=0)
    return get_top_articles(parse_top_news(top_news))
