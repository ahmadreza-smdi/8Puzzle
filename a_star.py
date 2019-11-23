from Node import *
import queue
import heapq	
from timeit import default_timer






priority_queue = []

def a_start(start , Goal):
	start_time = default_timer()
	heapq.heappush(priority_queue, start)
	count_extended_Nodes = 1
	#print("hefdsf")
	# print(heuristic(start))
	# print(start)
	# q.put(heuristic(start), start)
	# print(start.state)
	# ah = q.get()
	# print("HHHHHHHHHHHHHHHHHHHHHHeko")
	
	Extended_Nodes = []
	number_nodes = 0

	while start.done()!=True:
		# print("Reapet")
		# start = q.get()
		start = heapq.heappop(priority_queue)
		#print(start)
		#print("here")
		# print(heuristic(start))
		#start.print_nodes()
		
		number_nodes +=1
		if start.state ==Goal:
			print("___________________________")
			print ("You have reach Your Goal")
			print ("Number of The Extended Node is {}".format(count_extended_Nodes))
			temp = start
			counter = 0
			print("You Way Is Like This:")
			print("_______________________")
			while(temp!=None):
				counter+=1
				temp.print_nodes()
				print("****")
				temp = temp.father
			print("Number Of Actions Is : " + str(counter))
			duration = (default_timer() - start_time)
			print ("Time Past = ",duration)
			exit()
		else:
			count_extended_Nodes+=1
			Extended_Nodes.append(start)
			# print (start.state)
			start.Extend_nodes()
			if start.children["up"] not in Extended_Nodes:
				if start.children["up"] != None:
					# q.put(start.children["up"],heuristic(start))
					heapq.heappush(priority_queue, start.children["up"])

			if start.children["down"] not in Extended_Nodes:
				if start.children["down"] != None:
					# q.put(start.children["down"],heuristic(start))
					heapq.heappush(priority_queue, start.children["down"])



			if start.children["left"] not in Extended_Nodes:
				if start.children["left"] != None:
					# q.put(start.children["left"],heuristic(start))
					heapq.heappush(priority_queue, start.children["left"])

			if start.children["right"] not in Extended_Nodes:
				if start.children["right"] != None:
					# q.put(start.children["right"],heuristic(start))
					heapq.heappush(priority_queue, start.children["right"])
