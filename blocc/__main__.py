from random import randint

from blocc import Blocc

if __name__ is '__main__':
    start = Blocc({'message': 'lol'}, None)
    print("Start block:\n", start)

    bloccchain = [start]

    for _ in range(2):
        new = Blocc(
            {
                'random': randint(0, 9999)
            }, bloccchain[-1]
        )

        bloccchain.append(new)
        print("\nNew block #%d:\n" % new.index, new)
