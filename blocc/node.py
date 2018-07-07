import json

from flask import Flask, request, jsonify
from schema import Schema, And

from .bloccchain import yalls_bloccchain
from .royal_mint import RoyalMint

node = Flask(__name__)
royal_mint = RoyalMint()

transactions = []

transaction_schema = Schema({
    'from': And(str),
    'to': And(str),
    'amount': And(int),
})


@node.route('/transaction', methods=['POST'])
def transaction():
    new = request.get_json()

    # Check valid transaction
    try:
        transaction_schema.validate(new)
    except:
        return 'Invalid transaction schema', 400

    # Add to transaction list
    transactions.append(new)

    print('\nnew transaction:\n', json.dumps(new, indent=4))

    return jsonify(new), 200


@node.route('/mint/<minter>', methods=['GET'])
def mint(minter):
    global transactions
    new_mint = royal_mint.mint(minter, transactions).cereal
    transactions = []
    return jsonify(new_mint)


@node.route('/blocks', methods=['GET'])
def blocks():
    return jsonify(yalls_bloccchain.cereal)
