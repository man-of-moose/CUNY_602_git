import pandas as pd
import hashlib
from datetime import datetime
import random


class Transaction:
    def __init__(self, sender, receiver, value):
        self. sender = sender
        self.receiver = receiver
        self.value = value
        self.time = datetime.now()
        self.hash = None

    def generate_hash(self):
        m = hashlib.sha256()
        m.update(str.encode(self.sender))
        m.update(str.encode(self.receiver))
        m.update(str.encode(str(self.time)))
        m.update(str.encode(str(self.value)))
        m.update(str.encode(str(random.randint(0, 99))))

        self.hash = m.hexdigest()
