from .blocc_def import Blocc
from .bloccchain import yalls_bloccchain


class RoyalMint:
    def __init__(self):
        self.latest_proof = 1

    def pow(self):
        incrementor = self.latest_proof + 1
        while not (incrementor % 9 == 0 and
                   incrementor % self.latest_proof == 0):
            incrementor += 1
        self.latest_proof = incrementor
        return incrementorgit 

    def mint(self, minter, transactions):
        new_proof = self.pow()

        transactions.append({
            "from": "network",
            "to": minter,
            "amount": 1
        })

        minted = Blocc(
            {
                'transactions': transactions,
                'pow': new_proof
            }, yalls_bloccchain.latest
        )
        yalls_bloccchain.append(minted)

        return minted
