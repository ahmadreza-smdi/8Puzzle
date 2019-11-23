from Node import *
import queue
import heapq





priority_queue = []

def bestFirstSearch(start , Goal):
	
	heapq.heappush(priority_queue, start)
	count_extended_Nodes = 1
	Extended_Nodes = []

	while start.done()!=True:
		# print("Reapet")
		# start = q.get()
		start = heapq.heappop(priority_queue)
		#print(start)
		#print("here")
		start.print_nodes()
		number_nodes = 0
		number_nodes +=1
		print("****")
		if start.state ==Goal:
			print("___________________________")
			print ("You have reach Your Goal")
			print ("Number of The Extended Node is {}".format(count_extended_Nodes))
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