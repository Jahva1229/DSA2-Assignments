# PA1 Skeleton Code
# DSA2, fall 2025

# This code will read in the input, and put the values into lists.  It is up
# to you to properly represent this as a graph -- this code only reads in the
# input properly.

# How many input cases are there?
solution = []
n = int(input())

for _ in range(n):
	# read in the weights into wt, wf, wb, wc (wegiths for the edges of type tree, forward, backward, and cross, respectively)
	[wt,wf,wb,wc] = [int(x) for x in input().split(" ")]

	# read in the number of vertices and edges, respectively
	[v,e] = [int(x) for x in input().split(" ")]

	# all the edges in the graph -- the result is a list of tuples, such as: [('A', 'B'), ('B', 'C'), ... ]
	l = list(reversed(input().split(" ")))
	edges = [(l.pop(),l.pop()) for _ in range(len(l)//2)]

	# the start node and the node to print the pathogen load for
	(start,node) = input().split(" ")

	G = {}
	vertex_map = {}
	time = 0

	class Vertex:
		def __init__(self, name):
			self.name = name
			self.color = 'WHITE'
			self.d = float('inf')
			self.f = float('inf')
			self.pi = None
		
		def __hash__(self):
			return hash(self.name)
		
		def __eq__(self, other):
			return self.name == other.name

	def get_or_create_vertex(name):
		if name not in vertex_map:
			vertex_map[name] = Vertex(name)
		return vertex_map[name]

	def make_adj_list(edges):
		global G, vertex_map
		G = {}
		vertex_map = {}

		# build the graph as an adjacency list
		for (u,v) in edges:
			u = get_or_create_vertex(u)
			v = get_or_create_vertex(v)
			if u not in G:
				G[u] = []
			if v not in G.keys():
				G[v] = []
			G[u].append(v)
		
		# alphabetical order
		for u in G:
			G[u].sort(key=lambda x: x.name)


	def print_adj_list(G):
		for u in G:
			print(u.name, end=": ")
			for v in G[u]:
				print(v.name, end=" ")
			print()

	def dfs_visit(G, u):
		global time
		time += 1
		u.d = time
		u.color = 'GRAY'
		for v in G[u]:
			if v.color == 'WHITE':
				v.pi = u
				dfs_visit(G, v)
		u.color = 'BLACK'
		time += 1
		u.f = time

	def print_dfs(G):
		for u in G:
			print(f"Vertex: {u.name}, d: {u.d}, f: {u.f}, pi: {u.pi.name if u.pi else None}")

	def get_vertex_by_name(G, name):
		for u in G:
			if u.name == name:
				return u
		return None

	def classify_edge(u, v, wt, wf, wb, wc):
		if u.d == float('inf') or v.d == float('inf') or u.f == float('inf') or v.f == float('inf'):
			return 0
		elif v.pi is not None and v.pi == u:
			return wt
		elif v.d < u.d and u.f < v.f:
			return wb
		elif u.d < v.d and v.f < u.f:
			return wf
		else:
			return wc
		
	def pathogen_load(G, target, wt, wf, wb, wc):
		load = 0
		for u in G:
			for v in G[u]:
				if v == target:
					#print("Classifying edge:", u.name, v.name)
					#print(classify_edge(u, v, wt, wf, wb, wc))
					load += classify_edge(u, v, wt, wf, wb, wc)
		return load
			
		

	def main():
		#print("--- Adjacency List ---")
		make_adj_list(edges)
		#print_adj_list(G)

		#print("--- DFS Result---")
		start_vertex = get_vertex_by_name(G, start)
		dfs_visit(G, start_vertex)
		#print_dfs(G)

		#print("--- Pathogen Load ---")
		pathogen_load_value = pathogen_load(G, get_vertex_by_name(G, node), wt, wf, wb, wc)
		#print(f"Pathogen load for node {node}: {pathogen_load_value}")

		print(pathogen_load_value)
		


	if __name__ == "__main__":
		main()

