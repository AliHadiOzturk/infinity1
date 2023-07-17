from flask import Blueprint
from main import nok, ok

from common.exception import GenericException


news = Blueprint('news', __name__)

@news.route(f"<url>", methods=["GET"])
def content(url: str):
    try:
        # TODO: Implement site crawler
        return ok(None)
    except GenericException as err:
        return nok(err)