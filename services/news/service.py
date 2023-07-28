import json
from types import SimpleNamespace
import xmltodict
from bs4 import BeautifulSoup
import requests

from common.exception import Exceptions, GenericException
from common import logger
from models.news import News


#TODO: Implement for diffrent websites this only works for t24.com.tr
def content(url: str):
    try:
        uri = url if url.startswith("http") else f"https://{url}"

        uri = uri if uri.endswith("/rss") else f"{uri}/rss"

        rss_response = requests.get(uri)

        if rss_response.status_code != 200:
            raise Exceptions.ServerError("REquesting rss failed")

        data = json.loads(json.dumps(xmltodict.parse(rss_response.text)),
                          object_hook=lambda d: SimpleNamespace(**d))
        rss = data.rss

        news_list = []
        for news_item in rss.channel.item:
            news = News(news_item.title, "", "", "", news_item.pubDate, news_item.link)

            news_response = requests.get(news_item.link)

            if news_response.status_code != 200:
                raise Exceptions.ServerError(f"Requesting to {news_item.title} failed")

            soap = BeautifulSoup(news_response.text, "html.parser")

            # ps = soap.find_all("p")

            html_tags = soap.find_all("html")
            html = html_tags[1] if len(html_tags) > 1 else html_tags[0]
            content = html.text.replace("\n", "")
            news.description = content.split(".")[0]
            news.content = content
            news_list.append(news)

        return news_list

    except Exception as e:
        logger.error("Error occured", e)
        raise
