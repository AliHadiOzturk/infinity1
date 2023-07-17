import json


class GenericException(Exception):
    def __init__(self, code, message, key):
        self.code = code
        self.message = message
        self.key = key

        self.body = json.dumps({
            "code": self.code,
            "message": self.message,
            "key": self.key
        })

    def __str__(self):
        return repr(self.code)

    def encode(self):
        return self.body

    @classmethod
    def decode(cls, j):
        data = json.loads(j)
        c = data.get('code')
        m = data.get('message')
        k = data.get('key')
        e = Exception(data.get('payload'))

        return cls(c, m, k, e)


class Exceptions:

    #Implement 


    BadRequest = GenericException(400, "Bad Request", "bad_request")

    # Timeout = GenericException(408, "Request timed out", "timeout")
    NotFound = GenericException(404, "Not Found", "not_found")
    ServerError = GenericException(
        500, "Unexpected error occurred.", "unexpected_error")
