## Create the genesis block ##

import datetime as date

def createGenesisBlock():
    """ Manually create the genesis block"""
    return block(0,date.datetime.now(),"First Ever block","0")