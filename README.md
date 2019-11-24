# 8Puzzle
Solving the 8-puzzle problem with using of heuristic algorithm, such as A* algorithm,Gready(best first search) and BFS.
### what is 8-puzzle problem ?
The 8-puzzle problem is a puzzle invented and popularized by Noyes Palmer Chapman in the 1870s. It is played on a 3-by-3 grid with 8 square blocks labeled 1 through 8 and a blank square. Your goal is to rearrange the blocks so that they are in order. You are permitted to slide blocks horizontally or vertically into the blank square. The following shows a sequence of legal moves from an initial board position to the goal position.
### Heuristic Algorithms
#### A*
A* is an informed search algorithm, or a best-first search, meaning that it is formulated in terms of weighted graphs: starting from a specific starting node of a graph, it aims to find a path to the given goal node having the smallest cost (least distance travelled, shortest time, etc.). It does this by maintaining a tree of paths originating at the start node and extending those paths one edge at a time until its termination criterion is satisfied.

At each iteration of its main loop, A* needs to determine which of its paths to extend. It does so based on the cost of the path and an estimate of the cost required to extend the path all the way to the goal. Specifically, A* selects the path that minimizes  f(n)=g(n)+h(n) 

#### BFS
There are many ways to traverse graphs. BFS is the most commonly used approach.
BFS is a traversing algorithm where you should start traversing from a selected node (source or starting node) and traverse the graph layerwise thus exploring the neighbour nodes (nodes which are directly connected to source node). You must then move towards the next-level neighbour nodes.
As the name BFS suggests, you are required to traverse the graph breadthwise as follows:

1 - First move horizontally and visit all the nodes of the current layer

2 - Move to the next layer

#### Gready
A greedy algorithm is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage with the intent of finding a global optimum. In many problems, a greedy strategy does not usually produce an optimal solution, but nonetheless a greedy heuristic may yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time


## Prerequisites

What things you need to install the software and how to install them

the project is based on python, first step is installing python

#### Ubuntu
```
sudo apt-get update
sudo apt-get install python3.6
```
#### CentOS
```
sudo yum update
sudo yum install yum-utils
```
#### Fedora
```
sudo dnf install python36
```
#### Arch linux
```
packman -S python
```

## Running the project
All the files of the project is combined and all the modules are set to one file, so to run the 
project you just need to run.py file
```
python3 run.py
```

## Built With

* [Python](https://www.python.org/) - Programming language

## Authors

* **Ahmadreza Samadi** - *Programmer* - [Ahmadreza samadi](https://github.com/ahmadreza-smdi)

*Thanks for your attention.*
