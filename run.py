from Node import *
import os
from bfs import *
from mixing import *
from best_first_search import *
from a_star import *
from timeit import default_timer



def algorithm(matrix):
	print("__________________________")
	print("Which Algorithm you want to use ?\n")
	print("For A* Print A")
	print("For Best First Search Print G")
	print("For BFS print B")
	choose = input ().upper()

	if choose == "A":
		os.system("clear")
		print("You have choosen A* Algorithm")
		start = Nodes(matrix , None , 0 , 0 ,'A',None)
		a_start(start , Goal)

	if choose =="G":
		os.system("clear")
		print("You have choosen Mighty! Best First Algorithm")
		start = Nodes(matrix , None , 0 , 0 ,'G',None)
		bestFirstSearch(start , Goal)
	
	if choose == "B":
		os.system("clear")
		print("You have choosen bfs algorithm")
		start = Nodes(matrix , None , 0 , 0 ,'B',None)
		bfs(start,Goal)
	print("Wait Please I'm trying ...")

def get():
	print("_________________________")
	print(">>>>>>>> Inter The Combination :")
	matrix=[[0,0,0],[0,0,0],[0,0,0]]
	for x in range (0,3):
	    for y in range (0,3):
	        matrix[x][y]=int(input())
	print("__________________________")
	print (" Input = {}".format(matrix))
	return matrix




os.system('clear')
print("____________Welcom To Puzzle8 Solver______________by ARS__________\n")


print("How Would You Like To Continue ?")
print("________________________________")
print("1 - Mixup The Goal")
print("2 - Entering the combination")
choosee = input()

if choosee =='1':
	mixtime = int(input("How Many Times ?"))
	matrix = Get_mix(mixtime)
	algorithm(matrix)
	os.system('clear')
	print("Wait Please I'm trying ...")

if choosee == '2':
	matrix = get()
	algorithm(matrix)
	os.system('clear')





