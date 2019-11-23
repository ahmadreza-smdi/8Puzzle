import copy


def heuristic(node):
    """
    Manhattan distance
    """
    distance = 0
    m = node.state       
    for i in range(3):
        for j in range(3):
            if m[i][j] == Goal[i][j]: continue
            for k1 in range (3):
              for k2 in range (3):
                if m[i][j] == Goal[k1][k2]:
                  distance += abs(i - k1) + abs(j -  k2);
    # print(distance)

    return distance

class Nodes:

  def __init__ (self,state = None , father = None , cost = 0 , depth = 0,type_node = "G" ,move = None):
    self.state = state
    self.father = father
    self.cost = cost
    self.depth = depth
    self.move = move
    self.children = {'up':None, 'down':None,'left':None,'right':None}
    self.type_node = type_node


  def print_nodes(self):
    for i in range(3):
      for j in range(3):
        print(self.state[i][j] ,end='')
      print()


  def done(self):
    Goal = [[1,2,3],[4,5,6],[7,8,0]]
    if Goal == self.state :
      print ("Welldone you solved the Puzzle")
      return True


  def Extend_nodes(self):
	
    pm=moves(self.state)
    if pm['up'] != None:
      self.children['up']=Nodes(pm['up'], self, self.cost+1, self.depth+1, 'up')

    if pm['down'] !=None:
      self.children['down']=Nodes(pm['down'], self, self.cost+1, self.depth+1, 'down')

    if pm['left'] !=None:
      self.children['left']=Nodes(pm['left'], self, self.cost+1, self.depth+1, 'left')

    if pm['right'] !=None:
      self.children['right']=Nodes(pm['right'], self, self.cost+1, self.depth+1, 'right')

  def fn(self):
    return self.cost + heuristic(self.state)

  def __lt__(self, other):
    if self.type_node == "G":
      s = heuristic(self)
      x = heuristic(other)
      return s < x
      
    else:
      s = heuristic(self)+self.cost
      x = heuristic(other)+other.cost
      return s < x

def moves(node): 
    """
    Returns a list of all possible moves
    """ 
    pm = {'up':None, 'down':None,'left':None,'right':None} 

    m = node
    i = 0
    while 0 not in m[i]:
      i+=1
    j = m[i].index(0); #blank space (zero)

    if i > 0:                                   
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j];  #move up
      pm['up']=copy.deepcopy(m)
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j]; 
      
    if i < 2:                                   
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]   #move down
      pm['down']=copy.deepcopy(m)
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]

    if j > 0:                                                      
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]   #move left
      pm['left']=copy.deepcopy(m)
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]

    if j < 2:                                   
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]   #move right
      pm['right']=copy.deepcopy(m)
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]
    return pm 







Goal = [[1 , 2 , 3 ],[4 , 5 , 6],[7 , 8 , 0]]

