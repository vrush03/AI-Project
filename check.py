import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import queue

class BestFirstSearch(object):
	
	pq = pq = queue.PriorityQueue()
	heuristicValues = []
	numberOfNodes = 0
	def __init__(self, numberOfNodes):
		
		self.numberOfNodes = numberOfNodes
	
	def bestFirstSearch(self, adjMatrix, heuristicValues, source):
		evaluationNode = 0
		destinationNode = 0
		visited = {}
		self.heuristicValues = heuristicValues
		#print (self.heuristicValues[source])
		self.pq.put(Vertex(source, self.heuristicValues[source]))
		#print (self.pq.get().node)
		visited[source] = 1

		while not self.pq.empty():

			evaluationNode = self.getMinNode()
			#print (evaluationNode)

	def getMinNode(self):
			v = self.pq.get()
			return v.node		

class Vertex(object):
	"""docstring for Vertex"""
	heuristicValue = 0
	node = 0
	def __init__(self, node, heuristicValue):
		self.heuristicValue = heuristicValue
		self.node = node
	def compare(vertex1, vertex2):
		
		if (vertex1.heuriticValue < vertex2.heuriticValue):
			return -1
		if (vertex1.heuriticValue > vertex2.heuriticValue):
			return 1
		return 0



print ("Enter Number of Vertices:")
n = int(input())
adjMatrix = []

print ("Enter The Adjacency Matrix:")

for i in range(n):
	list1 = list(map(int,input().split(' ')))
	adjMatrix.append(list1)

print (adjMatrix)

print ("Enter Heuristics of the Node:")
heuristicValues = list(map(int,input().split(' ')))
print (heuristicValues)

print ("Enter Source:")
source = int(input())
print ("Result of Greedy Best First Search:")

BFS = BestFirstSearch(n)
BFS.bestFirstSearch(adjMatrix, heuristicValues, source)

