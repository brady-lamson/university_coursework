import unittest
import time

class Mammal:
    """ A Mammal class to further populate our animal kingdom """

    def __init__(self, species, name):
        """ mammal constructor can initialize class attributes """
        self.species = species
        self.name = name


    def eat(self, food):
        """ a method that will 'eat' in O(log(n)) time """
        food_count = food
        print(self.name, "the", self.species, "is about to eat")
        while food_count >= 1:
            time.sleep(0.1)
            food_count = food_count % 2
        print("    ", self.name, "is done eating!")

    def makeNoise(self):
        """ a method that should be implemented by children classes """
        raise NotImplementedError("this method should be implemented by child class")
    
    def getName(self):
        """ Returns the name of the animal. """
        return self.name

    def getSpecies(self):
        """ Returns the species of the animal. """
        return self.species

    def __eq__(self, other):
        """ Overrides the == operator to compare species of mammal. """
        return self.species == other.species


class Hippo(Mammal):
    """ A Hippo is a type of mammal that grunts a lot and, contrary to popular belief, can't swim! """
    def __init__(self, name):
        super().__init__(species='Hippo', name=name, )


    def makeNoise(self) -> str:
        """ Returns a noise suitable for a hippo. """
        # Note: Done as return with f string instead of print to ensure compatability with listenToMammal().
        return f"{self.name} grunts."


class Elephant(Mammal):
    """ An Elephant is a type of mammal that make low frequency rumbles and, unlike the hippo, can swim! """
    def __init__(self, name):
        super().__init__(species='Elephant', name=name)
    
    def makeNoise(self) -> str:
        """ Returns a noise suitable for an elephant. """
        return f"{self.name} rumbles."
    

class TestMammals(unittest.TestCase):
    """ a class that is derived from TestCase to allow for unit tests to run """

    def testInheritance(self):
        """ confirm that Elephant and Hippo are children classes of Mammal """
        self.assertTrue(issubclass(Elephant, Mammal) and issubclass(Hippo, Mammal))

    def testName(self):
        """ Confirm that getName() works as intended. """
        foo = Elephant('foo')
        bar = Hippo('bar')
        self.assertEqual(foo.getName(), 'foo')
        self.assertEqual(bar.getName(), 'bar')

    def testSpecies(self):
        """ Confirm that getSpecies() works as intended. """
        foo = Elephant('foo')
        bar = Hippo('bar')
        self.assertEqual(foo.getSpecies(), 'Elephant')
        self.assertEqual(bar.getSpecies(), 'Hippo')


# a function to help demonstrate polymorphism
def listenToMammal(Mammal):
    print(Mammal.makeNoise())


def main():
    """ a 'main' function to keep program clean and organized """
    print("-------------------- start main --------------------")

    # create instances of child classes
    ellie = Elephant("Ellie")
    henry = Hippo("Henry")

    # compare classes with overriden == operator, and call accessor method
    if(ellie == henry):
      print(ellie.getName(), "and", henry.getName(), "are of the same species")
    else:
      print(ellie.getName(), "and", henry.getName(), "are *not* of the same species")

    # polymorphism in action: treating different classes in the same way
    listenToMammal(ellie)
    listenToMammal(henry)

    # feed Ellie 10 bites of food (and see how long it takes!)
    ellie.eat(100)

    print("--------------------- end main ---------------------")


# this will run when the file is called as a standalone program (ex: python assign1.py)
if __name__ == "__main__":
    main()
    unittest.main()
