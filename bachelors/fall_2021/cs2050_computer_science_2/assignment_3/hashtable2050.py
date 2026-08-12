import unittest
import sympy

class HashTable:
    """
    A class implementing a basic hash table / hash map / associative array / etc.
    This is essentially the same as a Python dict(tionary) but by implementing
    our own version we will better understand how hash tables work internally.

    ADD ANY OTHER DOCUMENTATION YOU WANT HERE
    (REMOVE ANY AND ALL PLACEHOLDER COMMENTS IN ALL CAPS)
    """

    def __init__(self, size):
        """ INSERT COMMMENTS (IN YOUR WORDS) """
        self.size = size
        self.key_slots = [None] * self.size
        self.data_slots = [None] * self.size
        self.length = 0

    def __len__(self):
        """ 
        Returns number of items stored inside of the Hash Table.
        Note: This is different from the size of the hash table itself. For example
        A hash table of size 500 with 2 items inside of it will have a length of 2.
        """
        return self.length

    def loadFactor(self):
        """ 
        Utilizes size and length to determine how full the hash table is.
        """
        loadfactor = len(self) / self.size
        return loadfactor

    def put(self, key, data):
        """ INSERT COMMMENTS (IN YOUR WORDS) """
        hashvalue = self.hash(key)

        if self.loadFactor() >= .85:
            temp_size = self.size * 2
            temp_size = sympy.nextprime(temp_size)
            temp_hash_table = HashTable(temp_size)

            for position in self.key_slots:
                if(self.key_slots[position] != None):
                    
                # Assign old hash table to a temp value, rehash those values according to new size. 
                # Might require *in* operator for this to work properly. 
                # Rough thoughts are if (self.data_slots[value] exists)
                    # Refactor the whole dang thing. How to do that on the other hand....


        # an empty slot, so go ahead and add key and data and increment length counter up.
        if self.key_slots[hashvalue] == None:
            self.key_slots[hashvalue] = key
            self.data_slots[hashvalue] = data
            self.length += 1
        # slot was occuppied, so figure out what to do next
        else:
            # key is same as the key currently in this slot, so
            # replace data with the new data that was passed in
            if self.key_slots[hashvalue] == key:
                self.data_slots[hashvalue] = data
            # there was a collision with a different key, so use linear probing
            else:
                nextslot = self.rehash(hashvalue)
                while self.key_slots[nextslot] != None and self.key_slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                if self.key_slots[nextslot] == None:
                    self.key_slots[nextslot] = key
                    self.data_slots[nextslot] = data
                    self.length += 1
                else:
                    self.data_slots[nextslot] = data

    def hash(self, key):
        """ INSERT COMMMENTS (IN YOUR WORDS) """
        return key % self.size

    def rehash(self, oldhash):
        """ INSERT COMMMENTS (IN YOUR WORDS) """
        return (oldhash + 1) % self.size

    def get(self, key):
        """ INSERT COMMMENTS (IN YOUR WORDS) """
        startslot = self.hash(key)

        data = None
        stop = False
        found = False
        position = startslot
        while self.key_slots[position] != None and not found and not stop:
             if self.key_slots[position] == key:
                 found = True
                 data = self.data_slots[position]
             else:
                 position=self.rehash(position)
                 if position == startslot:
                     stop = True
        return data

    def __getitem__(self, key):
        """ INSERT COMMMENTS (IN YOUR WORDS) """
        return self.get(key)

    def __setitem__(self, key, data):
        """ INSERT COMMMENTS (IN YOUR WORDS) """
        self.put(key, data)

    # FOLLOW THE ASSIGNMENT 3 REQUIREMENTS (ADDING/MODIFYING METHODS AS NEEDED)
    # TO MAKE THIS A RELIABLE AND ROBUST IMPLEMENTATION OF A HASH TABLE
    # (AND REMOVE ANY AND ALL PLACEHOLDER COMMENTS IN ALL CAPS)


class TestHashTable(unittest.TestCase):
    """ Extend unittest.TestCase and add methods to test HashTable """

    def testKeysAfterPuts(self):
        """ Check that hashtable keys are as expected for a simple case """
        h = HashTable(7)
        h[6] = 'cat'
        h[29] = 'dog'
        expected = [None, 29, None, None, None, None, 6]
        self.assertEqual(h.key_slots, expected)

    # ADD TWO MORE UNIT TESTS OF YOUR OWN
    # (AND REMOVE ANY AND ALL PLACEHOLDER COMMENTS IN ALL CAPS)


def main():
    """ run any example/demo you want to when running as standalone program """
    h = HashTable(7)
    h[16] = 'cat'
    h[11] = 'dog'
    h[21] = 'bird'
    print("-"*26, "keys and values:", "-"*26)
    print(h.key_slots)
    print(h.data_slots)
    print(h[16] == 'cat')

def unittest_main():
    """ run unittest's main, which will run TestHashTable's methods """
    print("-"*25, "running unit tests", "-"*25)
    unittest.main()


# evaluates to true if run as standalone program (e.g. $ python hashtable.py)
if __name__ == '__main__':
    main()
    unittest_main()
