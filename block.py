## Block structure ##
import hashlib as hasher
import datetime as date

class Block: 
    
    def __init__(self, index, timestamp, data, previousHash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.hashBlock()

    def hashBlock(self):
        """ Definition of a block, with hashes of its data"""
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previousHash).encode('utf-8'))
        return sha.hexdigest()


## Create the genesis block ##
def createGenesisBlock():
    """ Manually create the genesis block"""
    return Block(0,date.datetime.now(),"First Ever block","0")

## Block creater ##
def nextBlock(previousBlock):
    this_index = previousBlock.index + 1
    this_timestamp = date.datetime.now()
    this_data = ("Hi!, I'm block "+str(this_index))
    this_hash = previousBlock.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

## create the blockchain
blockchain = [createGenesisBlock()]
previousBlock = blockchain[0]

## Add arbitary number of blocks
initBlocks = 10
for i in range(initBlocks):
    addBlock = nextBlock(previousBlock)
    blockchain.append(addBlock)
    previousBlock = addBlock
    print("Block #{0} has been added to the blockchain".format(addBlock.index))
    print("Block data: {0}\n".format(addBlock.data))
    print("Hash: {0}".format(addBlock.hash))
