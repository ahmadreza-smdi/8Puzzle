from Node import *
import random


def rev(i):
	if i == 'up':
		return 'down'
	elif i == 'down':
		return 'up'
	elif i == 'right':
		return 'left'
	elif i == 'left':
		return 'right'


def Get_mix(i):
	startt = Nodes(Goal ,None,0,0 ,None)
	last_move = ''

	while i != 0:
		pm = moves(startt.state)
		m = random.choice(['up' , 'down' ,'right' ,'left'])
		if m == rev(last_move):
			i += 1
		else:
			if pm[m] != None:
				startt.Extend_nodes()
				startt = startt.children[m]
				last_move = m
				startt.print_nodes()
				print("-------------------------")
			else:
				i += 1
		i -= 1
	print ("Your combination = {}".format(startt.state))
	return startt.state







