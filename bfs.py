from Node import *


def bfs(start,Goal):
	fring = []
	count_extended_Nodes = 0
	the_extended = []
	fring.append(start)
	# print(fring[0])
	# print(fring[0].state)

	while True:
		count_extended_Nodes+=1
		# print(fring[0])
		# print(fring[0].state)
		# print(fring[0])
		bfs_start = fring.pop(0)
		# print("here is where i print start",bfs_start)
		# print("here i print state",bfs_start.state)
		if bfs_start.state == Goal :
			print("___________________________")
			print ("You have reach Your Goal")
			print ("Number of The Extended Node is {}".format(count_extended_Nodes))
			temp = bfs_start
			counter = 0
			
			while(temp!=None):
				counter+=1
				temp.print_nodes()
				print("****")
				temp = temp.father
			print("number of actions is : " + str(counter))
			exit()
		else:
			the_extended.append(bfs_start.state)
			bfs_start.Extend_nodes()

			if bfs_start.children["up"] not in the_extended:
				if bfs_start.children["up"]!=None:
					fring.append(bfs_start.children["up"])
			
			if bfs_start.children["down"] not in the_extended:
				if bfs_start.children["down"]!=None:
					fring.append(bfs_start.children["down"])
				
			if bfs_start.children["left"] not in the_extended:
				if bfs_start.children["left"]!=None:
					fring.append(bfs_start.children["left"])
			
			if bfs_start.children["right"] not in the_extended:
				if bfs_start.children["right"]!=None:
					fring.append(bfs_start.children["right"])

