import json


class GenericException(Exception):
    def __init__(self, code, message, key, payload=None):
        self.code = code
        self.message = message
        self.key = key
        self.payload = payload

        payload = None
        try:
            payload = json.loads(self.payload)
        except:
            payload = self.payload if not isinstance(
                self.payload, Exception) else str(self.payload)

        self.body = json.dumps({
            "code": self.code,
            "message": self.message,
            "key": self.key,
            "payload": payload
        })

    def __str__(self):
        return repr(self.code)

    def encode(self):
        return self.body

    @classmethod
    def decode(cls, j):
        data = json.loads(j)
        code = data.get('code')
        message = data.get('message')
        key = data.get('key')
        exception = Exception(data.get('payload'))

        return cls(code, message, key, exception)


class Exceptions:

    #Implement 


    BadRequest = GenericException(400, "Bad Request", "bad_request")

    # Timeout = GenericException(408, "Request timed out", "timeout")
    NotFound = GenericException(404, "Not Found", "not_found")
    ServerError = (lambda payload=None: GenericException(
        500, "Unexpected error occurred.", "unexpected_error", payload))
