from dataclasses import dataclass
import json
import os
from dotenv import load_dotenv


# @dataclass
class Config:
    APP_NAME = None
    PORT = 5001  # default port
    LOG_LEVEL = "ERROR"

    def load(self):
        # IF override not specified then change of environment variables not writes
        load_dotenv(override=True)

        self.APP_NAME = os.environ.get("APP_NAME")
        self.PORT = os.environ.get("PORT")
        self.LOG_LEVEL = os.environ.get("LOG_LEVEL") if not None else "ERROR"

        return self
