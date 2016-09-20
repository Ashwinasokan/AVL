import avl
tree = avl.node(9)
numbers = [5,10,0,6,11,-1,1,2]
for number in numbers:
	tree = tree.insert(number)
print tree.inOrder()
print tree.preOrder()
print tree.balance()
print tree.height
print tree.value
tree = tree.delete(10)
print tree.inOrder()
print tree.preOrder()
print tree.balance()
print tree.height
print tree.value
