import hashlib
from datetime import datetime

class Block():
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.timestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f")
        self.previous_hash = None
        self.hash = None

class BlockChain():
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, value):
        block = Block(value)
        block.hash = calc_hash(value + block.timestamp)
        if (self.head is None):
            self.head = block
        else:
            block.previous = self.head
            block.previous_hash = self.head.hash
            self.head = block
        self.count = self.count + 1

def calc_hash( data):
    sha = hashlib.sha256()

    hash_str = data.encode('utf-8')

    sha.update(hash_str)

    return sha.hexdigest()

blockchain = BlockChain()

assert blockchain.head == None
assert blockchain.count == 0

blockchain.push('first')

assert type(blockchain.head) == Block
assert blockchain.head.value == 'first'
assert blockchain.count == 1
assert blockchain.head.previous_hash == None
assert type(blockchain.head.timestamp) == str
assert blockchain.head.hash == calc_hash(blockchain.head.value + blockchain.head.timestamp)

blockchain.push('second')

assert blockchain.head.previous_hash == blockchain.head.previous.hash

