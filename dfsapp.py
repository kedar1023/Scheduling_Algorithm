# Python program to print DFS traversal from a 
# given given graph 
from collections import defaultdict 

finalroute = []
# This class represents a directed graph using 
# adjacency list representation 
class Graph: 

	# Constructor 
	def __init__(self): 

		# default dictionary to store graph 
		self.graph = defaultdict(dict)

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		finalroute[u].append(v)

	# A function used by DFS 
	def DFSUtil(self,v,visited): 

		# Mark the current node as visited and print it 
		visited[v] = True
		print (v)

		# Recur for all the vertices adjacent to this vertex 
		for i in self.graph[v]: 
			if visited[i] == False: 
				self.DFSUtil(i, visited) 


	# The function to do DFS traversal. It uses 
	# recursive DFSUtil() 
	def DFS(self,v): 

		# Mark all the vertices as not visited 
		visited = [False]*(len(self.graph)) 

		# Call the recursive helper function to print 
		# DFS traversal 
		self.DFSUtil(v,visited) 


# Driver code 
# Create a graph given in the above diagram 
g = Graph() 
g.addEdge(str("Manapa")) 
g.addEdge(str("Manapa")) 
g.addEdge(str("Shanivarwada")) 
g.addEdge(str("Lokmandal") )
g.addEdge(str("Alandi") )
g.addEdge(str("Alandi") )

print ("Following is DFS application starts from MANAPA")
g.DFS("Manapa") 

# This code is contributed by Neelam Yadav 
