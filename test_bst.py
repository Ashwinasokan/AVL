import unittest
import bst
import random

def is_bst(tree):
	if tree.left != None and tree.left.value > tree.value:
		return False
	if tree.right != None and tree.right.value < tree.value:
		return False
	if tree.left == None:
		left = True
	else:
		left = is_bst(tree.left)
	if tree.right == None:
		right = True
	else:
		right = is_bst(tree.right)
	return left and right

def create_random_bst():
	tree = bst.node(0)
	numbers = random.sample(range(-100,100),20)
	for number in numbers:
		tree = tree.insert(number)
	return tree

class TestBst(unittest.TestCase):
	
	def test_insert(self):
		tree = bst.node(5)
		tree.insert(8)
		self.assertIsNotNone(tree.search(8))
		self.assertIsNone(tree.search(0))

	def test_isBst(self):
		tree = create_random_bst()
		self.assertTrue(is_bst(tree))
	
	def test_highest(self):
      		tree = create_random_bst()
		tree = tree.insert(1000)
		self.assertEqual(tree.highest().value,1000)

	def test_lowest(self):
		tree = create_random_bst()
		tree = tree.insert(-1000)
		self.assertEqual(tree.lowest().value,-1000)

	def test_successor(self):
		tree = create_random_bst()
		randomn = random.randint(-100,100)
		tree = tree.insert(randomn).insert(randomn+1)
		self.assertEqual(tree.search(randomn).successor().value,randomn+1)

	def test_predecessor(self):
		tree = create_random_bst()
		randomn = random.randint(-100,100)
		tree = tree.insert(randomn).insert(randomn-1)
		self.assertEqual(tree.search(randomn).predecessor().value,randomn-1)

	def test_delete(self):
		tree = create_random_bst()
		randomn = random.randint(-100,100)
		tree = tree.insert(randomn)
		self.assertIsNotNone(tree.search(randomn))
		tree = tree.delete(randomn)
		self.assertIsNone(tree.search(randomn))

if __name__ == '__main__':
    unittest.main()
