## Block structure ##
import hashlib as hasher

class Block: 
    
    def __init__(self, index, timestamp, date, previousHash):
        self.index = index
        self.timestamp = timestamp
        self.date = date
        self.previousHash = previousHash
        self.hash = self.hashBlock()

    def hashBlock(self):
        """ Definition of a block, with hashes of its data"""
        sha = hasher.sha256()
        sha.update(str(self.index) + str(self.timestamp) + str(self.date) + str(self.previousHash))
        return sha.hexdigest()