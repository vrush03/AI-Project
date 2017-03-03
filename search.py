import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import queue

class BestFirstSearch(object):
	
	pq = queue.PriorityQueue()
	heuristicValues = []
	numberOfNodes = 0
	def __init__(self, numberOfNodes):
		
		self.numberOfNodes = numberOfNodes
	
	def bestFirstSearch(self, adjMatrix, heuristicValues, source):
		evaluationNode = 0
		destinationNode = 0
		visited = [0 for x in range(100)]
		self.heuristicValues = heuristicValues
		#print (self.heuristicValues[source])
		self.pq.put(Vertex(source, self.heuristicValues[source]))
		#print (self.pq.get().node)
		visited[source] = 1

		while not self.pq.empty():

			evaluationNode = self.getMinNode()
			destinationNode = 0

			print (evaluationNode, )

			while (destinationNode < self.numberOfNodes):
				
				#print (self.heuristicValues[destinationNode])
				v = Vertex(destinationNode, self.heuristicValues[destinationNode])
				
				if (adjMatrix[evaluationNode][destinationNode] != 9999 and evaluationNode!=destinationNode and visited[destinationNode] == 0):
					self.pq.put(v)
					visited[destinationNode] = 1
				destinationNode = destinationNode + 1

	def getMinNode(self):
			v = self.pq.get()
			return v.node		

class Vertex:
	"""docstring for Vertex"""
	heuristicValue = 0
	node = 0
	def __init__(self, node, heuristicValue):
		self.heuristicValue = heuristicValue
		self.node = node
	def __lt__(self, other):
		
		return self.heuristicValue < other.heuristicValue



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

