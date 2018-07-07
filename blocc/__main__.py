from random import randint

from blocc import Blocc, yalls_bloccchain
from .node import node

if __name__ is '__main__':
    start = Blocc({'message': 'lol'}, None)
    print("Start block:\n", start)

    yalls_bloccchain.append(start)

    for _ in range(2):
        new = Blocc(
            {
                'random': randint(0, 9999)
            }, yalls_bloccchain.latest
        )

        yalls_bloccchain.append(new)
        print("\nNew block #%d:\n" % new.index, new)

    node.run('0.0.0.0', port=8123)
