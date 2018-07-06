import hashlib
import json
from datetime import datetime
from random import randint


def enc(thingy):
    if isinstance(thingy, bytes):
        return thingy

    return str(thingy).encode('utf-8')



class Blocc:
    def __init__(self, data, prev):
        self.timestamp = datetime.now().isoformat()

        if isinstance(prev, Blocc):
            self.prev = prev
            self.index = prev.index + 1
            assert self.timestamp > prev.timestamp
        elif prev is None:
            self.prev = prev
            self.index = 0

        self.data = data

        # Check data is JSON serializable
        try:
            self.data_json = json.dumps(data)
        except TypeError as e:
            raise e

        self.hash = self.blocc_hash()

    def blocc_hash(self):
        return hashlib.sha256(
            enc(self.index) +
            enc(self.timestamp) +
            enc(self.data_json) +
            enc(self.prev)
        ).hexdigest()

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            indent=4
        )

    def __repr__(self):
        return self.toJSON()


if __name__ == '__main__':
    bloccchain = [Blocc({'message': 'lol'}, None)]

    for _ in range(3):
        bloccchain.append(
            Blocc(
                {
                    'random': randint(0, 9999)
                }, bloccchain[-1]
            )
        )
        print('Added blocc #%d' % bloccchain[-1].index)

    print(bloccchain[-1])
