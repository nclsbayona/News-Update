import requests

# API Key: 20ad2407c8b140db8d0034e4c067e1f3
def getLatestNews(country_code: str, api_key: str) -> list:
    the_news = requests.get(
        "https://newsapi.org/v2/top-headlines?country={}&apiKey={}".format(
            country_code, api_key
        )
    ).json()
    return list(the_news.get("articles"))


def printArticle(article: dict) -> None:
    print()
    print("From:", article.get("source").get("name"))
    print("Author:", article.get("author"))
    print("Title:", article.get("title"))
    print("Description:", article.get("description"))
    print("Url:", article.get("url"))
    print("Image Url:", article.get("urlToImage"))
    print("Publish date:", article.get("publishedAt"))


news = getLatestNews("co", "20ad2407c8b140db8d0034e4c067e1f3")
for art in news:
    printArticle(art)