from functools import wraps

from flask import Flask, Response
from flask_cors import CORS
from werkzeug.exceptions import NotFound
from common import config, logger, GenericException, Exceptions


def response_ok(data, code=200, headers={}):
    request_headers = {
        'content-type': 'application/json',
        **headers
    }

    return Response(data, code, request_headers)


def not_ok(error):
    request_headers = {
        'content-type': 'application/json',
    }

    return Response(error.body, error.code, request_headers)


def create_app(name):
    flask_app = Flask(name)
    logger.info(
        f"Web server mode is {'development' if flask_app.config['DEBUG'] else 'production'}")

    # a.json_encoder = models.DefaultEncoder

    CORS(flask_app, origins="*",
         expose_headers=["Authorization", "metadata"], supports_credentials=True)

    @flask_app.errorhandler(NotFound)
    def not_found(e):
        return not_ok(Exceptions.NotFound)
    
    @flask_app.errorhandler(Exception)
    def handle_exception(e):
        if isinstance(e, GenericException) and e is not Exceptions.NotFound:
            print(e)
            return not_ok(e)

        return not_ok(Exceptions.ServerError())

    return flask_app


app = create_app(config.APP_NAME)
