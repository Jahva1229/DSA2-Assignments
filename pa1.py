# PA1 Skeleton Code
# DSA2, fall 2025

# This code will read in the input, and put the values into lists.  It is up
# to you to properly represent this as a graph -- this code only reads in the
# input properly.

# How many input cases are there?
n = int(input())
G = {}

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


def make_adj_list(edges):
	global G
	# build the graph as an adjacency list
	for (u,v) in edges:
		u = Vertex(u)
		v = Vertex(v)
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

def dfs(G):
	global time
	time = 0
	for u in G:
		if u.color == 'WHITE':
			dfs_visit(G, u)

def print_dfs(G):
	for u in G:
		print(f"Vertex: {u.name}, d: {u.d}, f: {u.f}, pi: {u.pi.name if u.pi else None}")

def get_vertex_by_name(G, name):
	for u in G:
		if u.name == name:
			return u
	return None

def main():
	print("--- Adjacency List ---")
	make_adj_list(edges)
	print_adj_list(G)

	print("--- DFS Result---")
	dfs(G)
	print_dfs(G)

	print("--- Pathogen Load ---")


if __name__ == "__main__":
	main()