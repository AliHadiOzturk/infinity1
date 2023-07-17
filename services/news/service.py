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
        u = url if url.startswith("http") else f"https://{url}"

        u = u if u.endswith("/rss") else f"{u}/rss"

        resp = requests.get(u)

        if resp.status_code != 200:
            raise Exceptions.ServerError("REquesting rss failed")

        data = json.loads(json.dumps(xmltodict.parse(resp.text)),
                          object_hook=lambda d: SimpleNamespace(**d))
        rss = data.rss

        news = []
        for n in rss.channel.item:
            ns = News(n.title, "", "", "", n.pubDate, n.link)

            nresponse = requests.get(n.link)

            if nresponse.status_code != 200:
                raise Exceptions.ServerError(f"Requesting to {n.title} failed")

            soap = BeautifulSoup(nresponse.text, "html.parser")

            ps = soap.find_all("p")

            htmls = soap.find_all("html")
            html = htmls[1] if len(htmls) > 1 else htmls[0]
            content = html.text.replace("\\n", "")
            ns.description = html.text.split("\\.")[0]
            ns.content = html.text
            news.append(ns)

        return news

    except Exception as e:
        logger.error("Error occured", e)
        raise
