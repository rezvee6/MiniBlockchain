## Block structure ##

class Block: 
    
    def __init__(self, index, timestamp, date, previousHash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.hashBlock()

    