import hashlib
import json
from datetime import datetime

from .misc import byte_me


class Blocc:
    def __init__(self, data, prev):
        self.timestamp = datetime.now().isoformat()

        if isinstance(prev, Blocc):
            self.prev = prev.hash
            self.index = prev.index + 1
            assert self.timestamp > prev.timestamp
        elif prev is None:
            self.prev = None
            self.index = 0

        self.data = data
        assert isinstance(self.data_json, str)

        self.hash = self.blocc_hash()

    @property
    def data_json(self):
        # Check data is JSON serializable
        try:
            return json.dumps(self.data)
        except TypeError as e:
            raise e

    def blocc_hash(self):
        return hashlib.sha256(
            byte_me(self.index) +
            byte_me(self.timestamp) +
            byte_me(self.data_json) +
            byte_me(self.prev)
        ).hexdigest()

    @property
    def cereal(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    @property
    def json(self):
        return json.dumps(self.cereal, indent=4)

    def __repr__(self):
        return self.json
