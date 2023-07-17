import json
from .base import Base


class Packet(Base):

    def __init__(self, status, payload) -> None:
        super().__init__()
        self.status = status
        self.payload = payload

    def encode(self):
        p = []
        if isinstance(self.payload, list):
            for item in self.payload:
                p.append(item.as_dict())

        self.payload = p if len(p) > 1 else self.payload

        return json.dumps(self.as_dict())
