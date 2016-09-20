class node(object):
	def __init__(self, value = None, parent = None, left = None, right = None):
		self.value = value
		self.parent = parent
		self.left = left
		self.right = right

	def __repr__(self, level=0): #print tree
		ret = "\t"*level+repr(self.value)+"\n"
		if self.left is not None:
			ret += self.left.__repr__(level+1)
		if self.right is not None:
                        ret += self.right.__repr__(level+1)
		return ret

	def search(self, value): #returns Node corresponding to the value if present
    		if self.value == value:
			return self
		else:
			if value < self.value:
				if self.left != None:
					return self.left.search(value)
				else:
					return None
			else:
				if self.right != None:
					return self.right.search(value)
				else:
					return None

	def insert(self, item): #insert item return self
		if self.value == item:
			return self
		else:
			if item < self.value:
				if self.left != None:
					self.left.insert(item)
					return self
				else:
					self.left = node(item)
					return self
			else:
				if self.right != None:
					self.right.insert(item)
					return self
				else:
					self.right = node(item)
					return self

	def highest(self): # return highest value node 
		if self.right != None:
			return self.right.highest()
		else:
			return self

	def lowest(self): # return lowest value node
		if self.left != None:
			return self.left.lowest()
		else:
			return self

	def successor(self): # return next value node in order
		if self.right != None:
			return self.right.lowest()
		x = self
		y = self.parent
		while y != None and x == y.right:
			x = y
			y = y.parent
		return y

	def predecessor(self): # return previous value node in order 
		if self.left != None:
			return self.left.highest()
		x = self
		y = self.parent
		while y != None and x == y.left:
			x = y
			y = y.parent
		return y

	def delete(self, value): # delete the node with value and return the resulting tree root
		if value == self.value:
			if self.left == None and self.right == None:
				self.parent = None
				return None
			elif self.left == None:
				self.right.parent = self.parent
				self.parent = None
				return self.right
			elif self.right == None:
				self.left.parent = self.parent
				self.parent = None
				return self.left
			else:
				successor = self.successor()
				successor.right = self.delete(successor)
				successor.left = self.left
				successor.parent = self.parent
				self.parent = None
				return successor
		else:
			if value < self.value and self.left != None:
				self.left = self.left.delete(value)
			if value > self.value and self.right != None:
				self.right = self.right.delete(value)
			return self
