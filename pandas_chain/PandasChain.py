import datetime as dt
import hashlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import unittest
from datetime import datetime
import random
from Block import Block
import uuid


class PandasChain:
    # 5 pts - Complete this constructor
    def __init__(self, name):
        self.__name = name.upper() # Convert name to upper case and store it here
        self.__chain = [] # Create an empty list
        self.__id = hashlib.sha256(
            str(str(uuid.uuid4()) + self.__name + str(dt.datetime.now())).encode('utf-8')).hexdigest()
        # Create a sequence ID and set to zero
        self.__prev_hash = None # Set to None
        self.__seq_id = 0
        self.__current_block = Block(0) # Create a new Block
        print(self.__name, 'PandasChain created with ID', self.__id, 'chain started.')

    # 5 pts - This method should loop through all committed and uncommitted blocks and display all transactions in them
    def display_chain(self):
        for block in self.__chain:
            transactions = block.transactions
            for index, row in transactions.iterrows():
                print(row)

        for index, row in self.__current_block.transactions:
            print(row)

    # This method accepts a new transaction and adds it to current block if block is not full.
    # If block is full, it will delegate the committing and creation of a new current block
    def add_transaction(self, s, r, v):
        if self.__current_block.get_size() >= 10:
            self.__commit_block(self.__current_block)
        else:
            self.__current_block.add_transaction(s, r, v)

    # 10 pts - This method is called by add_transaction if a block is full (i.e 10 or more transactions).
    # It is private and therefore not public accessible. It will change the block status to committed, obtain the merkle
    # root hash, generate and set the block's hash, set the prev_hash to the previous block's hash, append this block
    # to the chain list, increment the seq_id and create a new block as the current block
    def __commit_block(self, block):
        if len(self.__chain) == 0:
            block.prev_hash = None
        else:
            block.prev_hash = self.__chain[-1].block_hash

        merkle = block.get_simple_merkle_root()

        m = hashlib.sha256()
        m.update(str.encode(str(block.prev_hash))) # add previous hash to hash
        m.update(str.encode(str(self.__id))) # add chain id to hash
        m.update(str.encode(str(datetime.now()))) # add current timestamp to hash
        m.update(str.encode(str(self.__seq_id))) # add sequence id to hash
        m.update(str.encode(str(random.randint(0, 99)))) # add random number to hash
        m.update(str.encode(str(merkle)))

        block.block_hash =  m.hexdigest()
        block.set_status("COMMITTED")
        self.__chain.append(block)
        print('Block committed')

        self.__seq_id += 1
        self.__current_block = Block(self.__seq_id)
        print('New Block Instantiated')

    # 10 pts - Display just the metadata of all blocks (committed or uncommitted), one block per line.
    # You'll display the sequence Id, status, block hash, previous block's hash, merkle hash and total number (count)
    # of transactions in the block
    def display_block_headers(self):
        for block in self.__chain:
            block.display_header()

        self.__current_block.display_header()


    # 5 pts - return int total number of blocks in this chain (committed and uncommitted blocks combined)
    def get_number_of_blocks(self):
        committed = len(self.__chain)

        return committed + 1

    # 10 pts - Returns all of the values (Pandas coins transferred) of all transactions from every block as a single list
    def get_values(self):
        values = []

        for block in self.__chain:
            transactions = block.transactions
            for index, row in transactions:
                values.append(row['value'])

        for index, row in self.__current_block.transactions:
            values.append(row['value'])

        return values


# class Block:
#     # 5 pts for constructor
#     def __init__(self, seq_id, prev_hash):
#         self.__seq_id =  # Set to what's passed in from constructor
#         self.__prev_hash =  # From constructor
#         self.__col_names = ['Timestamp', 'Sender', 'Receiver', 'Value', 'TxHash']
#         self.__transactions =  # Create a new blank DataFrame with set headers
#         self.__status =  # Initial status. This will be a string.
#         self.__block_hash = None
#         self.__merkle_tx_hash = None

    # 5 pts -  Display on a single line the metadata of this block. You'll display the sequence Id, status,
    # block hash, previous block's hash, merkle hash and number of transactions in the block
    # def display_header(self):
    #     pass

    # 10 pts - This is the interface for how transactions are added
    # def add_transaction(self, s, r, v):
    #     ts =  # Get current timestamp
    #     tx_hash =  # Hash of timestamp, sender, receiver, value
    #     new_transaction =  # Create DataFrame with transaction data (a DataFrame with only 1 row)
    #     # Append to the transactions data

    # 10 pts -Print all transactions contained by this block
    # def display_transactions(self):
    #     pass

    # 5 pts- Return the number of transactions contained by this block
    # def get_size(self):
    #     pass

    # 5 pts - Setter for status - Allow for the change of status (only two statuses exist - COMMITTED or UNCOMMITTED).
    # There is no need to validate status.
    # def set_status(self, status):
    #     pass

    # 5 pts - Setter for block hash
    # def set_block_hash(self, hash):
    #     self.

    # 10 pts - Return and calculate merkle hash by taking all transaction hashes, concatenate them into one string and
    # hash that string producing a "merkle root" - Note, this is not how merkle tries work but is instructive
    # and indicative in terms of the intent and purpose of merkle tries
    # def get_simple_merkle_root(self):
    #     pass

    # def get_values(self):
    #     pass


class TestAssignment4(unittest.TestCase):
    def test_chain(self):
        block = Block(1, "test")
        self.assertEqual(block.get_size(), 0)
        block.add_transaction("Bob", "Alice", 50)
        self.assertEqual(block.get_size(), 1)
        pandas_chain = PandasChain('testnet')
        self.assertEqual(pandas_chain.get_number_of_blocks(), 1)
        pandas_chain.add_transaction("Bob", "Alice", 50)
        pandas_chain.add_transaction("Bob", "Alice", 51)
        pandas_chain.add_transaction("Bob", "Alice", 52)
        pandas_chain.add_transaction("Bob", "Alice", 53)
        pandas_chain.add_transaction("Bob", "Alice", 53)
        pandas_chain.add_transaction("Bob", "Alice", 53)
        pandas_chain.add_transaction("Bob", "Alice", 53)
        pandas_chain.add_transaction("Bob", "Alice", 53)
        pandas_chain.add_transaction("Bob", "Alice", 53)
        pandas_chain.add_transaction("Bob", "Alice", 53)
        pandas_chain.add_transaction("Bob", "Alice", 53)
        self.assertEqual(pandas_chain.get_number_of_blocks(), 2)
        pandas_chain.add_transaction("Bob", "Alice", 50)
        pandas_chain.add_transaction("Bob", "Alice", 51)
        pandas_chain.add_transaction("Bob", "Alice", 52)
        pandas_chain.add_transaction("Bob", "Alice", 53)
        pandas_chain.add_transaction("Bob", "Alice", 53)
        pandas_chain.add_transaction("Bob", "Alice", 53)
        pandas_chain.add_transaction("Bob", "Alice", 53)
        pandas_chain.add_transaction("Bob", "Alice", 53)
        pandas_chain.add_transaction("Bob", "Alice", 53)
        pandas_chain.add_transaction("Bob", "Alice", 53)
        pandas_chain.add_transaction("Bob", "Alice", 53)
        self.assertEqual(pandas_chain.get_number_of_blocks(), 3)


if __name__ == '__main__':
    unittest.main()