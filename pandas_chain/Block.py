from Transaction import Transaction
import pandas as pd
import time
import hashlib
from datetime import datetime
import random


class Block:
    def __init__(self, sequence_id, prev_hash=None):
        self.sequence_id = sequence_id
        self.status = "UNCOMMITTED"
        self.merkle = None
        self.block_hash = None
        self.prev_hash = prev_hash
        self.transactions = pd.DataFrame(columns=['sender', 'receiver', 'value', 'time', 'hash'])
        self.size = 0

    def get_size(self):
        return self.size

    def add_transaction(self, sender, receiver, value):
        t = Transaction(sender, receiver, value)
        t.generate_hash()

        row = self.transactions.shape[0]
        self.transactions.loc[row] = [t.sender, t.receiver, t.value, t.time, t.hash]
        self.size += 1

    def get_simple_merkle_root(self):
        hashes = list(self.transactions['hash'])
        hashes = [str(x) for x in hashes]
        concat_hash = ",".join(hashes)

        m = hashlib.sha256()
        m.update(str.encode(concat_hash))

        self.merkle = m.hexdigest()

    def display_header(self):
        print([self.sequence_id, self.status, self.block_hash, self.prev_hash, self.merkle, self.size])

    def display_transactions(self):
        ret = list(self.transactions['value'])

        print(ret)

    def get_size(self):
        return self.size

    def set_status(self, status):
        self.status = status

    def set_block_hash(self, hash):
        self.block_hash = hash


# block = Block(0)
# transaction_1 = Transaction("Bob", "Mary", 10)
# transaction_1.generate_hash()
#
# transaction_2 = Transaction("Jeff", "Billy", 5)
# transaction_2.generate_hash()

# block.add_transaction("Bob", "Mary", 10)
# time.sleep(5)
# block.add_transaction("Jeff", "Billy", 5)
#
# block.generate_merkle()
#
# block.display_header()

# breakk = 5
