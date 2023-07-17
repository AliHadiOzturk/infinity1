from functools import wraps

from flask import Flask, Response
from flask_cors import CORS
from werkzeug.exceptions import NotFound
from common import config, logger, GenericException, Exceptions


def ok(data, code=200, headers={}):
    h = {
        'content-type': 'application/json',
        **headers
    }

    return Response(data, code, h)


def nok(error):
    h = {
        'content-type': 'application/json',
    }

    return Response(error.body, error.code, h)


def create_app(name):
    a = Flask(name)
    logger.info(
        f"Web server mode is {'development' if a.config['DEBUG'] else 'production'}")

    # a.json_encoder = models.DefaultEncoder

    CORS(a, origins="*",
         expose_headers=["Authorization", "metadata"], supports_credentials=True)

    @a.errorhandler(NotFound)
    def not_found(e):
        return nok(Exceptions.NotFound)
    
    @a.errorhandler(Exception)
    def handle_exception(e):
        if isinstance(e, GenericException) and e is not Exceptions.NotFound:
            print(e)
            return nok(e)

        return nok(Exceptions.ServerError)

    return a


app = create_app(config.APP_NAME)
