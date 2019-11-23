from Node import *
from run import *
# start.Extend_nodes()
# print(start.children["up"].state)
from queue import Queue
q = Queue()

q.put(start)
start.Extend_nodes()
q.put(start.children)
for i in range(5):
	a = q.get()
	print (a.state)
