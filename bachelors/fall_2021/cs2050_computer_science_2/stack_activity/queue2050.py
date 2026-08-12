class Queue:
	def __init__(self):
		""" Queue Constructor, class uses a list to hold items """
		self.queue = []

	def __str__ (self):
		return "Contents of queue: ", + str(self.queue)

	def isEmpty(self):
		""" Checks to see if the queue is empty. Returns boolean. """
		return self.queue == []

	def enqueue(self, new_item):
		""" 
		Adds new item to the queue at the back 
		(right side of the python list)  
		"""
		self.queue.append(new_item)

	def dequeue(self):
		""" Remove and returning item at the front (left, so index[0]) """
		return self.queue.pop(0)

	def peek(self):
		""" return item at the front (but dont remove it) """
		return self.queue[0]		

	def size(self):
		""" return number of items in the queue """
		return len(self.queue)