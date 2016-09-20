import avl
import random
import sys
import numpy
import math
import time
import matplotlib.pyplot as plt
import collections
from timeit import default_timer as timer
n = []
b = []
h = []
l = []
r = []
c = collections.Counter()
temp = collections.Counter()
t = collections.Counter()
nt = []
times = []
for i in range(2,20):
	tree = avl.node(random.randint(-sys.maxsize,sys.maxsize))
	numbers = numpy.random.random_integers(-math.pow(2,i), math.pow(2,i), math.pow(2,i))
	for idx, number in enumerate(numbers):
		start = timer()
		tree = tree.insert(number)
		end = timer()
		c[idx] += 1
		temp[idx] += (end - start)
	n.append(math.pow(2,i))
	b.append(tree.balance())
	h.append(tree.height)
	l.append(avl.node.left_rotation_count)
	r.append(avl.node.right_rotation_count)
	print "i:" + str(i) +" n:" + str(math.pow(2,i)) + " b:" + str(tree.balance()) + " h:" + str(tree.height) + " l:" + str(avl.node.left_rotation_count) + " r:" + str(avl.node.right_rotation_count)
	avl.node.left_rotation_count = avl.node.right_rotation_count = 0
for index, (key, value) in enumerate(c.items()):
    t[key] = float(temp[key]) / float(value)
od = collections.OrderedDict(sorted(t.items()))
for index, (key, value) in enumerate(od.items()):
	nt.append(key)
	times.append(math.log(value,2))
fig = plt.figure()
ax1 = fig.add_subplot(111)
#ax1.scatter(n, l, s=10, c='r', marker="s", label='leftRotations')
#ax1.scatter(n, r, s=10, c='g', marker="o", label='RightRotations')
#ax1.scatter(n, h, s=10, c='b', marker="v", label='Height')
ax1.scatter(nt, times, s=10, c='r', marker="s", label='Time')
plt.legend(loc='upper left')
plt.xlabel('No of Nodes')
plt.ylabel('Insertion Time average in seconds')
plt.show()
