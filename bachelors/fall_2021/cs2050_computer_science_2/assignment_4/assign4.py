import unittest
import hashlib
import datetime


class Block:
    """ A block is a container for data. It contains a data string, a hash and its own timestamp! """

    def __init__(self, data, previous_hash):
        """ Initializes the block object with all of the necessary variables. """
        self.timestamp = datetime.datetime.now()
        self.data_string = data
        self.previous_hash = previous_hash
        self.hash = self.do_hash()
        self.next_block = None
        

    def getNextBlock(self):
        """ Returns next block in the chain. """
        return self.next_block


    def getDataString(self):
        """ Returns data stored in the current block. """
        return self.data_string


    def getBlockHash(self):
        """ Returns this blocks hash digest. """
        return self.hash


    def setNextBlock(self, next_block):
        """ Sets the next block in the chain. """
        self.next_block = next_block


    def __str__(self):
        """ Return a string representation of this block """
        return '\nCreated: ' + str(self.timestamp) + \
            '\nData: ' + str(self.data_string) + \
            '\nPrevHash: ' + str(self.previous_hash) + \
            '\nHash: ' + str(self.hash) + '\n'


    def do_hash(self):
        """ Compute and return the hash digest for this block """
        sha256 = hashlib.sha256()
        sha256.update(str(self.timestamp).encode('utf-8') + \
            str(self.data_string).encode('utf-8') + \
            str(self.previous_hash).encode('utf-8'))
        return sha256.hexdigest()


class BlockChain:
    """ 
    The block chain class allows linking multiple blocks together. This functions similar to a linked list and 
    the implemention is, in fact, quite similar. Blocks can be added, retrieved, and the entire chain can be printed out as well.
    The information output when printed is the timestamp, hash, and the previous blocks hash.
    """

    def __init__(self):
        """ Initializes the BlockChain with a genesis block (like the head in a linked list) and a latest_block. """
        self.genesis_block = Block('Genesis Block', 0)
        self.latest_block = self.genesis_block


    def __str__(self):
        """ Prints out the entirety of the block chain. """
        current = self.genesis_block
        output = ''
        while current != None:
            output = "".join([output, str(current), '\n'])
            current = current.getNextBlock()
        return output


    def retrieveBlock(self, index):
        """ Returns block at the specified index. """
        count = 0
        index = int(index)
        current = self.genesis_block
        while count < index:
            current = current.getNextBlock()
            count += 1
        return current


    def addNewBlock(self, new_data):
        """ Adds a new block to the chain and updates the latest_block variable. """
        new_block = Block(new_data, self.latest_block.getBlockHash())
        self.latest_block.setNextBlock(new_block)
        self.latest_block = self.latest_block.getNextBlock() 


class TestChain(unittest.TestCase):

    def verifyHashing(self, block, previous):
        """ A helper method to faciliate checks on two consecutive blocks """
        block_hash = block.do_hash()
        return block.getBlockHash() == block_hash and previous.getBlockHash() == block.previous_hash

    def testVerify(self):
        """ Confirm that the second block in the chain uses the genesis block's hash """
        genesis_block = Block("Genesis Block", "0")
        new_block = Block("More data", genesis_block.getBlockHash())
        self.assertTrue(self.verifyHashing(new_block, genesis_block))

    def testGetDataString(self):
        """ Verifies that the Block class' getDataString method works as intended. """
        foo = Block('foo', 0)
        self.assertEqual(foo.getDataString(), 'foo')

    def testAddNewBlock(self):
        """ Confirms that addNewBlock correctly updates the latest_block variable. """
        blockchain = BlockChain()
        blockchain.addNewBlock('foo')
        self.assertEqual(blockchain.latest_block.getDataString(), 'foo')

    def testRetrieveBlock(self):
        """ Confirms that retrieveBlock returns the correct block. """
        blockchain = BlockChain()
        blockchain.addNewBlock('foo')
        self.assertEqual(blockchain.retrieveBlock(1), blockchain.latest_block)


if __name__ == '__main__':
    blockchain = BlockChain()
    while True:
        input_req = input('\n (A)dd new block, (P)rint full blockchain, (R)etrieve one specific block (Q)uit program: ').upper()
        input_req = input_req.upper()
        if input_req  == 'A':
            blockchain.addNewBlock(input('    Enter the data string for the new block: '))
        elif input_req  == 'P':
            print(blockchain)
        elif input_req  == 'R':
            index_to_retrieve = input('    Insert the index of the block to retrieve (0-based index): ')
            print(blockchain.retrieveBlock(index_to_retrieve))
        elif input_req  == 'Q':
            break
    unittest.main()