class Stack:
	def __init__(self):
		""" Stack Constructor, class uses a list to hold items """
		self.stack = []

	def isEmpty(self):
		""" Checks to see if the stack is empty. Returns boolean. """
		return self.stack == []

	def push(self, new_item):
		""" Appends new item to the stack  """
		self.stack.append(new_item)

	def pop(self):
		""" Does stuff """
		return self.pop()

	def peek(self):
		""" Stuff """
		return self.stack[-1]		