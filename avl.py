class node(object):
	left_rotation_count = 0
	right_rotation_count = 0
	def __init__(self, value = None, parent = None, left = None, right = None, height = 1):
		self.value = value
		self.parent = parent
		self.left = left
		self.right = right
		self.height = height

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

	def rightRotate(self): #Rotate tree right
		node.right_rotation_count += 1
		y = self
		x = y.left
		if x == None:
			T2 = None
		else:
			T2 = x.right
	
		x.right = y
		if y != None: 
			y.parent = x
		y.left = T2
		if T2 != None:
			T2.parent = y

		y.height = max(0 if y.left == None else y.left.height, 0 if y.right == None else y.right.height) + 1
		x.height = max(0 if x.left == None else x.left.height,0 if x.right == None else x.right.height) + 1
		x.parent = None
		return x

	def leftRotate(self): #Rotate tree left
		node.left_rotation_count += 1
		x = self
		y = x.right
		T2 = y.left
		
		y.left = x
		if x != None:
			x.parent = y
		x.right = T2
		if T2 != None:
			T2.parent = x

		x.height = max(0 if x.left == None else x.left.height,0 if x.right == None else x.right.height) + 1
		y.height = max(0 if y.left == None else y.left.height,0 if y.right == None else y.right.height) + 1
		y.parent = None
		return y

	def insert(self, item): #insert item return self
		if self.value == item:
			return self
		else:
			if item < self.value:
				if self.left != None:
					self.left = self.left.insert(item)
					self.left.parent = self
				else:
					self.left = node(item)
					self.left.parent = self
			else:
				if self.right != None:
					self.right = self.right.insert(item)
					self.right.parent = self
				else:
					self.right = node(item)
					self.right.parent = self

			self.height = max(0 if self.left == None else self.left.height,0 if self.right == None else self.right.height) + 1

			balance = self.balance()

			if balance > 1 and self.left != None and item < self.left.value:
				return self.rightRotate()
			if balance < -1 and self.right != None and item > self.right.value:
				return self.leftRotate()
			if balance > 1 and self.left != None and item > self.left.value:
				self.left = self.left.leftRotate()
				self.left.parent = self
				return self.rightRotate()
			if balance < -1 and self.right != None and item < self.right.value:
				self.right = self.right.rightRotate()
				self.right.parent = self
				return self.leftRotate()
			return self
	
	def balance(self): # balance factor of node
		left = 0
		right = 0
		if self.left != None:
			left = self.left.height
		if self.right != None:
			right = self.right.height
		return left - right

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
		print self.inOrder()
		print value
		if value == self.value:
			if self.left == None and self.right == None:
				self.parent = None
				self = None
			elif self.left == None:
				self.right.parent = self.parent
				self.parent = None
				self = self.right
			elif self.right == None:
				self.left.parent = self.parent
				self.parent = None
				self = self.left
			else:
				successor = self.successor()
				successor.right = self.delete(successor)
				successor.left = self.left
				successor.parent = self.parent
				self.parent = None
				self = successor
		else:
			if value < self.value and self.left != None:
				self.left = self.left.delete(value)
				if self.left != None:
					self.left.parent = self
			if value > self.value and self.right != None:
				self.right = self.right.delete(value)
				if self.right != None:
					self.right.parent = self
		if self == None:
			return self
		
		self.height = max(0 if self.left == None else self.left.height,0 if self.right == None else self.right.height) + 1
		
		balance = self.balance()

		if balance > 1 and (self.left == None or self.left.balance >= 0):
			return self.rightRotate()
		if balance > 1 and self.left != None and self.left.balance < 0:
			self.left = self.left.leftRotate()
			self.left.parent = self
			return self.rightRotate()
		if balance < -1 and (self.right == None or self.right.balance <= 0):
			return self.leftRotate()
		if balance < -1 and self.right != None and self.right.balance > 0:
			self.right = self.right.rightRotate()
			self.right.parent = self
			return self.leftRotate()
		return self

	def inOrder(self):
		ret = ""
		if self.left != None:
			ret += self.left.inOrder()
		ret += "Value " + str(self.value) + " "
		ret += "L " + str(self.lowest().value) + " "
		ret += "H " + str(self.highest().value) + " "
		if self.parent != None:
			ret += "Parent " + str(self.parent.value) + " "
		if self.predecessor() != None:
			ret += "P " + str(self.predecessor().value) + " "
		if self.successor() != None:
			ret += "S " + str(self.successor().value) + " "
		ret += "\n"
		if self.right != None:
			ret += self.right.inOrder()
		return ret

	def preOrder(self):
		ret = " " + str(self.value) + " "
		if self.left != None:
                        ret += self.left.preOrder()
		if self.right != None:
                        ret += self.right.preOrder()
                return ret
