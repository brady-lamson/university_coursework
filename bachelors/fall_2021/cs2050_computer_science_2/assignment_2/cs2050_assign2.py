from datetime import time
from lists2050 import UnorderedList
import random
import unittest
import sys

class QueueLL:
    """ 
    A class that allows for the collection of objects in a sequence. It follows a first in first out (FIFO) order. 
    This class allows one to add (enqueue) items to the back of the queue, to return items from the front (dequeue),
    among a few other features.
    """

    def __init__(self):
        """ Create the one field/attribute needed for our QueueLL class """
        self.queue = UnorderedList()

    def __str__(self):
        """ Prints out entirety of linked list. """
        #print(self.queue)
        return str(self.queue)

    def isEmpty(self):
        """ Return True if the list is empty, False otherwise """
        return self.queue.isEmpty()

    def enqueue(self, item):
        """ Adds new item to back of queue, returns nothing. """
        self.queue.append(item)

    def dequeue(self):
        """ Return and remove item at the front of the queue. """
        return self.queue.pop(0)

    def peek(self):
        """ Return item at the front of the queue, but don't remove it. """
        ret_val = self.queue.pop(0)
        self.queue.add(ret_val)
        return ret_val

    def size(self):
        """ Return the number of Nodes currently in the queue. """
        return self.queue.size()

    def convert2List(self):
        """ Converts current linked list to a python list. """
        self.queue.convert2List()


class TestQueueLL(unittest.TestCase):
    """ Test class to ensure method functionability. """

    def testQueueOrder(self):
        # Ensures that the front of the linked list is where it is intended to be
        test_queue = QueueLL()
        test_queue.enqueue(5)
        test_queue.enqueue(12)
        test_queue.enqueue('cat')
        self.assertEqual(test_queue.dequeue(), 5)

    def testSize(self):
        # Ensure testSize reads the size correctly
        test_queue = QueueLL()
        test_queue.enqueue(97)
        test_queue.enqueue('dog')
        test_queue.enqueue(5)
        self.assertEqual(test_queue.size(), 3)

    def testIsEmpty(self):
        # Ensure that isEmpty returns correct boolean
        test_queue = QueueLL()
        test_queue.enqueue(97)
        test_queue.enqueue('dog')
        test_queue.enqueue(5)
        self.assertEqual(test_queue.isEmpty(), False)

    def testPeekReturn(self):
        # Ensure peek returns correct value.
        test_queue = QueueLL()
        test_queue.enqueue(97)
        test_queue.enqueue('dog')
        test_queue.enqueue(5)
        self.assertEqual(test_queue.peek(), 97)

    def testPeekSize(self):
        # Ensure that peek doesn't alter the size of the linked list.
        test_queue = QueueLL()
        test_queue.enqueue(97)
        test_queue.enqueue('dog')
        test_queue.enqueue(5)
        test_queue.peek()
        self.assertEqual(test_queue.size(), 3)


class TrafficSimulatorQueue(QueueLL):
    """
    A class to simulate traffic arriving and leaving an intersection with a stop
    light.  As with all simulations, time is discretized so that each loop
    iteration represents one (1) second of time.

    Fields:
      * queue [from inheritance] - the internal structure that holds the queue
      * traffic_light_state - current status of the traffic light, either 'red' or 'green'
      * time_steps_needed_for_1_car_to_exit - time steps (e.g. 'seconds') needed for front car to exit intersection
      * prob_arrival - probability that an automobile arrives on any given iteration/epoch
      * time_steps_light_is_red - number of time steps (e.g. 'seconds') the traffic light is red
      * time_steps_light_is_green - number of time steps (e.g. 'seconds') the traffic light is green

    Methods:
      * __init__() - constructor to initialize class fields/attributes
      * isEmpty() [from inheritance]
      * enqueue(new_item) [from inheritance]
      * dequeue() [from inheritance]
      * size() [from inheritance]
      * peek() [from inheritance]
      * setTimeForCarToExit(time_to_exit) - modifies the time steps required for a car to leave the intersection
      * setProbabilityArrival(prob_arrival) - modify the probablity that a car arrives at any given time step
      * setMinutesRed(min_red) - modify the number of minutes the traffic light is red for (and convert to seconds/time_steps)
      * setMinutesGreen(min_red) - modify the number of minutes the traffic light is red for (and convert to seconds/time_steps)
      * checkForArrivingAuto() - check to see if a car arrives (intended to be called at each time step)
      * simulateTraffic(n) - simulate traffic for n cycles of red and green lights, starting with red first and
                             printing status, queue, etc. as the simulation is carried out
    """

    def __init__(self):
        """ Creates the fields/attributes needed for our class. """
        super().__init__()
        self.traffic_light_state = "red"
        self.time_steps_needed_for_1_car_to_exit = 3
        self.prob_arrival = 0
        self.time_steps_light_is_red = 0
        self.time_steps_light_is_green = 0

    def isEmpty(self):
        """ Return True if the list is empty, False otherwise """
        return super().isEmpty()

    def enqueue(self, item):
        """ Adds new item to back of queue, returns nothing. """
        super().enqueue(item)
    
    def dequeue(self):
        """ Returns and removes item from front of queue. """
        return super().dequeue()

    def size(self):
        """ Returns number of nodes in the linked list. """
        return super().size()

    def peek(self):
        """ Returns item at front of queue, but does not remove it."""
        return super().peek()

    def setTimeForCarToExit(self, time_to_exit):
        """ 
        Modifies the time necessary for the car to exit the intersection. Input time is in seconds. 
        Defaults to 3 if not used.
        """
        if (time_to_exit > 0):
            self.time_steps_needed_for_1_car_to_exit = time_to_exit
        else:
            sys.exit("Not valid input for setTimeForCarToExit(). Must be a positive numerical value.")

    def setProbabilityArrival(self, prob_arrival):
        """ Modify the probablity that a car arrives at any given time step. """
        if (prob_arrival < 1 and prob_arrival >= 0):
            self.prob_arrival = prob_arrival
        else:
            sys.exit("Not valid input for setProbabilityArrival(). Value must be in the interval [0,1)")

    def setMinutesRed(self, min_red):
        """ Modifies the number of minutes the traffic light is red. Converts input minutes to seconds. """
        if (min_red >= 0):
            self.time_steps_light_is_red = min_red * 60
        else:
            sys.exit("Not valid input for setMinutesRed(). Must be a numerical value greater than or equal to 0.")

    def setMinutesGreen(self, min_green):
        """ Modifies the number of minutes the traffic light is green. Converts input minutes to seconds. """
        if (min_green >= 0):
            self.time_steps_light_is_green = min_green * 60
        else:
            sys.exit("Not valid input for setMinutesRed(). Must be a numerical value greater than or equal to 0.")
    
    def getSecondsRed(self):
        """ Returns the seconds the light will stay red. Intended for testing purposes. """
        return self.time_steps_light_is_red

    def getSecondsGreen(self):
        """ Returns the seconds the light will stay green. Intended for testing purposes. """
        return self.time_steps_light_is_green

    def checkForArrivingAuto(self):
        """
        Generate a random number between 0 and 1, then see if it less than
        self.prob_arrival. If it is, then add a new auto/car to the queue.
        """
        r = random.random()

        if r < self.prob_arrival:
            car_arriving = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            self.enqueue(car_arriving)

    def simulateTraffic(self, number_redgreen_cycles):
        """ Run the simulation where each iteration of the while loop represents 1 second. """
        print("Traffic light is red, current queue size = " + str(self.size()))

        # i is the total number of time_steps when the number of cycles is taken into account.  
        time_steps = (self.time_steps_light_is_green + self.time_steps_light_is_red)
        i = time_steps * number_redgreen_cycles
        
        # Changes value of i_light depending on the state of the light.
        if self.traffic_light_state == "red":
            i_light = self.time_steps_light_is_red
        else:
            i_light = self.time_steps_light_is_green

        while i > 0:
            # cars can arrive regardless of whether the light is red or green
            self.checkForArrivingAuto()

            # light is red, so just decrement the light counter, i_light
            # once i_light has counted down to 0, then set everything needed to
            # change it to greeen
            if self.traffic_light_state == "red":
                i_light -= 1
                if i_light == 0:
                    # Changes light to green and sets i_light to time_steps_light_is_red
                    print("Traffic light changing to green, current queue size = " + str(self.size()) + ", queue:")
                    print(" "*2, self)
                    i_light = self.time_steps_light_is_green
                    self.traffic_light_state = "green"

            # light is green, so just decrement light counter AND check to see if
            # time_steps_needed_for_1_car_to_exit iterations have passed (if so, removed a car from the queue)
            # once i_light has counted down to 0, then set everything needed to change the light to red
            else:
                i_light -= 1
                if i % self.time_steps_needed_for_1_car_to_exit == 0 and self.size() > 0:
                    car_leaving = self.dequeue()
                    print(" "*4, "car,", car_leaving, ", exiting intersection")
                if i_light == 0:
                    self.traffic_light_state = 'red'
                    i_light = self.time_steps_light_is_red
                    print("Traffic light changing to red, current queue size = " + str(self.size()) + ", queue:")
                    print(" "*2, self)
            i -= 1


class TestTrafficSimulatorQueue(unittest.TestCase):
    """ Test class to ensure method functionality. """

    # Traffic simulator exclusive tests
    def testMinutesRed(self):
        test_traffic = TrafficSimulatorQueue()
        test_traffic.setMinutesRed(2)
        self.assertEqual(test_traffic.getSecondsRed(), 2*60)

    def testMinutesGreen(self):
        test_traffic = TrafficSimulatorQueue()
        test_traffic.setMinutesGreen(5)
        self.assertEqual(test_traffic.getSecondsGreen(), 5*60)

    # Inheritance tests to ensure proper functionality carried over from QueueLL
    def testQueueOrder(self):
        test_traffic = TrafficSimulatorQueue()
        test_traffic.enqueue('F')
        test_traffic.enqueue('O')
        test_traffic.enqueue('O')
        self.assertEqual(test_traffic.dequeue(), 'F')

    def testSize(self):
        test_traffic = TrafficSimulatorQueue()
        test_traffic.enqueue('F')
        test_traffic.enqueue('O')
        test_traffic.enqueue('O')
        self.assertEqual(test_traffic.size(), 3)
    
    def testIsEmpty(self):
        test_traffic = TrafficSimulatorQueue()
        test_traffic.enqueue('F')
        test_traffic.enqueue('O')
        test_traffic.enqueue('O')
        self.assertEqual(test_traffic.isEmpty(), False)


if __name__ == '__main__':

    print('='*30, 'Simulation 1:', '='*30)
    ts = TrafficSimulatorQueue()
    
    # Sets time steps required for car to leave intersection to 3 (equivelant to 3 simulated seconds).
    ts.setTimeForCarToExit(3)

    # set probability that a car arrives on any given second (i.e. loop # iteration) to 50%
    ts.setProbabilityArrival(0.50)

    # set the light to be red for 2 minutes (needs to be converted to seconds inside)
    ts.setMinutesRed(2)

    # set the light to be green for 1 minute (needs to be converted to seconds inside)
    ts.setMinutesGreen(1)

    # run simulation for two red-green cycles (i.e. red -> green -> red -> green)
    ts.simulateTraffic(2)

    print("Traffic simulator queue size at end of simulation =", ts.size())
    print("Traffic simulator queue at end of simulation:")
    print(ts)
    unittest.main()
