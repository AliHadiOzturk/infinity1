from flask import Blueprint
from main import nok, ok
from models import Packet
from . import service

from common.exception import GenericException


news = Blueprint('news', __name__)

@news.route(f"<url>", methods=["POST"])
def content(url: str):
    try:
        response = service.content(url)
        # TODO: COnsider using enum for http response types
        return ok(Packet(200, response).encode())
    except GenericException as err:
        return nok(err)