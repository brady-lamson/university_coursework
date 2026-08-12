class Deque:
    def __init__(self):
        """ Queue Constructor, class uses a list to hold items """
        self.deque = []

    def __str__(self):
        return str(self.deque)

    def isEmpty(self):
        """ Checks to see if the deque is empty. Returns boolean. """
        return self.deque == []

    def addFront(self, item):
        """ Add an  item to the front (left, i.e. index 0) of the python list """
        self.deque.insert(0, item)

    def addRear(self, item):
        """ Adds an item to the back (right, i.e. index(n-1) ) of the python list """
        self.deque.append()

    def removeFront(self):
        """ Remove and return first item in the list (on the left, index 0) """
        return self.deque.pop(0)
    
    def removeRear(self):
        """ Remove and return final item in the list (on the right, index(n-1) )"""
        return self.deque.pop(-1)

    def peekFront(self):
        """ Shows first item on the left of the python list (index 0)"""
        return self.deque[0]

    def peekRear(self):
        """ Returns final item in the list (on the right, index(n-1))"""
        return self.deque[-1]