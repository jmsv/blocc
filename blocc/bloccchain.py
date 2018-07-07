import json

from .blocc_def import Blocc


class Bloccchain():
    def __init__(self):
        self.__chain = []
        print('\n\n~~~~~~~~~~ new bloccchain ~~~~~~~~~~\n\n')

    def append(self, new_blocc):
        # Check new blocc is a Blocc
        assert isinstance(new_blocc, Blocc)
        # Check chain link or initial blocc
        assert self.latest is None or new_blocc.prev is self.latest.hash

        self.__chain.append(new_blocc)

    @property
    def latest(self):
        if len(self.__chain) == 0:
            return None
        return self.__chain[-1]

    @property
    def cereal(self):
        return json.loads(json.dumps(
            self.__chain, default=lambda o: o.__dict__))

    @property
    def json(self):
        return json.dumps(self.cereal, indent=4)

    def __repr__(self):
        return self.json


yalls_bloccchain = Bloccchain()
