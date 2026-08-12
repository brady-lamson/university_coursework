import unittest
import time

class Mammal:
    """ A Mammal class to further populate our animal kingdom """

    def __init__(self, species):
        """ mammal constructor can initialize class attributes """
        self.species = species
        self.name = None

    def eat(self, food):
        """ a method that will 'eat' in O(n) time """
        i = food
        print(self.name, "the", self.species, "is about to eat")
        while i >= 1:
            time.sleep(0.1)
            i -= 1
        print("    ", self.name, "is done eating!")

    def makeNoise(self):
        """ a method that should be implemented by children classes """
        raise NotImplementedError("this method should be implemented by child class")

    # ADD ANY OTHER BASE CLASS METHODS YOU NEED/WANT TO HERE


# THE FOLLOWING TWO CLASSES NEED TO BE COMPLETED, AND YOU
# NEED TO REPLACE/DELETE ALL OF THE ELLIPSES SHOWN BELOW

class Hippo ...
    ...
    ...

class Elephant ...
    ...
    ...


class TestMammals(unittest.TestCase):
    """ a class that is derived from TestCase to allow for unit tests to run """

    def testInheritance(self):
        """ confirm that Elephant and Hippo are children classes of Mammal """
        self.assertTrue(issubclass(Elephant, Mammal) and issubclass(Hippo, Mammal))

    # ADD YOUR OTHER TESTS HERE, AT LEAST 2 MORE TO FULFILL TESTING RUBRIC CRITERION


def main():
    """ a 'main' function to keep program clean and organized """
    print("-------------------- start main --------------------")

    # create instances of child classes
    e = Elephant("Ellie")
    h = Hippo("Henry")

    # compare classes with overriden == operator, and call accessor method
    if(e == h):
      print(e.getName(), "and", h.getName(), "are of the same species")
    else:
      print(e.getName(), "and", h.getName(), "are *not* of the same species")

    # a function to help demonstrate polymorphism
    def listenToMammal(Mammal):
      print(Mammal.makeNoise())

    # polymorphism in action: treating different classes in the same way
    listenToMammal(e)
    listenToMammal(h)

    # feed Ellie 10 bites of food (and see how long it takes!)
    e.eat(100)

    print("--------------------- end main ---------------------")


# this will run when the file is called as a standalone program (ex: python assign1.py)
if __name__ == "__main__":
    main()
    unittest.main()
