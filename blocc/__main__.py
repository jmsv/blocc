from blocc import Blocc
from random import randint

if __name__ is '__main__':
    bloccchain = [Blocc({'message': 'lol'}, None)]

    for _ in range(3):
        bloccchain.append(
            Blocc(
                {
                    'random': randint(0, 9999)
                }, bloccchain[-1]
            )
        )

    print(bloccchain)
