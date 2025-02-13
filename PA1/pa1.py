import heapq

# PA1 Skeleton Code
# DSA2, spring 2025

# This code will read in the input, and put the values into lists.  It is up
# to you to properly represent this as a graph -- this code only reads in the
# input properly.

def read_input():
	# Read in the values for the number of side roads, main roads, and highways
	[s,m,h] = [int(x) for x in input().split(" ")]
	# Read in the side road edges
	tmp = input().split(" ")
	side_road_edges = sorted([(int(tmp[i]),int(tmp[i+1]),int(tmp[i+2]),int(tmp[i+3]),int(tmp[i+4])) for i in range(0,5*s,5)])
	# Read in the main road edges
	tmp = input().split(" ")
	main_road_edges = sorted([(int(tmp[i]),int(tmp[i+1]),int(tmp[i+2]),int(tmp[i+3]),int(tmp[i+4])) for i in range(0,5*m,5)])
	# Read in the highway edges
	tmp = input().split(" ")
	highway_edges = sorted([(int(tmp[i]),int(tmp[i+1]),int(tmp[i+2]),int(tmp[i+3]),int(tmp[i+4])) for i in range(0,5*h,5)])
	# Read in how many test cases there will be
	num_test_cases = int(input())
	# Read in each test case
	test_cases = []
	for _ in range(num_test_cases):
		tmp = input().split(" ")
		test_cases.append((int(tmp[0]),int(tmp[1]),int(tmp[2]),int(tmp[3])))

	# Generate a list of the nodes fron the edges read in
	side_road_nodes = []
	main_road_nodes = []
	highway_nodes = []
	all_nodes = []
	for (x1,y1,x2,y2,w) in side_road_edges:
		side_road_nodes.append((x1,y1))
		side_road_nodes.append((x2,y2))
	side_road_nodes = sorted(list(set(side_road_nodes))) # remove duplicates
	for (x1,y1,x2,y2,w) in main_road_edges:
		main_road_nodes.append((x1,y1))
		main_road_nodes.append((x2,y2))
	main_road_nodes = sorted(list(set(main_road_nodes))) # remove duplicates
	for (x1,y1,x2,y2,w) in highway_edges:
		highway_nodes.append((x1,y1))
		highway_nodes.append((x2,y2))
	highway_nodes = sorted(list(set(highway_nodes))) # remove duplicates
	all_nodes = sorted(list(set(side_road_nodes+main_road_nodes+highway_nodes))) # combine and remove duplicates

	# At this point, the data structures are as follows.  You may not need all of
	# these in your code.
	#
	# - `s`, `m`, and `h` contain the (integer) number of side road edges, main
	#   road edges, and highway edges, respectively
	#
	# - Edge data structures:
	#   - `side_road_edges` contains a list of 5-tuples that represent the edges
	#     of the side roads.  Example: [(0, 0, 0, 1, 1), (0, 0, 1, 0, 1), ...].
	#     The 5-tuple is (x1,y1,x2,y2,2), where (x1,y1) is one end of the edge,
	#     (x2,y2) is the other end, and w is the weight of the edge.  All values
	#     are integers.  This list is sorted.  Note that this only has the edges
	#     in one direction, but they are bi-directional edges.
	#   - `main_road_edges` has the edges for the main roads, in the same form as
	#     the edges for the side roads
	#   - `highway_edges` has the edges for the main roads, in the same form as
	#     the edges for the side roads
	#
	# - Node data structures:
	#   - `side_road_nodes` contain all the nodes that connect to a side road as a
	#     list of 2-tuples; this list is sorted
	#   - `main_road_nodes` contain all the nodes that connect to a main road as a
	#     list of 2-tuples; this list is sorted
	#   - `highway_nodes` contain all the nodes that connect to a highway as a
	#     list of 2-tuples; this list is sorted
	#   - `all_nodes` contain all the nodes in the graph as a list of 2-tuples;
	#     this list is sorted
	#
	# - Test case data structures:
	#   - `num_test_cases` is how many test cases there are
	#   - `test_cases` is the test cases themselves, as a list of 4-tuples.
	#     Example: [(4, 0, 3, 8), (1, 1, 3, 7), (5, 1, 8, 3)].  Each tuple is of
	#     the form (x1,y1,x2,y2), which means that the test case is to find the
	#     route from (x1,y1) to (x2,y2).  The tuples in this list are in the
	#     order they occur in the input file.

	return (s,m,h,side_road_edges,main_road_edges,highway_edges,side_road_nodes,main_road_nodes,highway_nodes,all_nodes,num_test_cases,test_cases)

# output() function -- given a list of coordinates (as 2-tuples) and the
# (integer) distance, this function will output the result in the correct
# format for the auto-grader
def output(path,dist):
	print(dist)
	print(len(path))
	for (x,y) in path:
		print(x,y)
	print()



#YOUR CODE HERE
def create_adj_list(E, V):
	adj_list = {}

	# Initialize adjacency list
	for v in V:
		adj_list[v] = []

	# Add edges to adjacency list
	for e in E:
		v1 = (e[0], e[1])
		v2 = (e[2], e[3])
		w = e[4]

		# Check if edge is already in adjacency list
		if (v2, w) not in adj_list[v1]:
			adj_list[v1].append((v2, w))
		if (v1, w) not in adj_list[v2]:
			adj_list[v2].append((v1, w))
	
	return adj_list

def print_adj_list(adj_list):
	for key in adj_list:
		edges = " -> ".join([f"{v}({w})" for v, w in adj_list[key]])
		print(f"{key} -> {edges}")

def dijkstra(adj_list, start, end):
	dist = {node: float("inf") for node in adj_list}
	done = {node: False for node in adj_list}
	pred = {node: None for node in adj_list}

	pq = []
	heapq.heappush(pq, (0, start))
	dist[start] = 0

	while pq:
		current_dist, current = heapq.heappop(pq)

		if done[current]:
			continue
		done[current] = True

		for v, w in adj_list[current]:
			new_dist = dist[current] + w
			if new_dist < dist[v]:
				dist[v] = new_dist
				pred[v] = current
				heapq.heappush(pq, (new_dist, v))

	path = []
	current = end
	while current:
		path.append(current)
		current = pred[current]
	return dist[end], len(path), path[::-1]

	




def main():
	# Read in input
	(s,m,h,side_road_edges,main_road_edges,highway_edges,side_road_nodes,main_road_nodes,highway_nodes,all_nodes,num_test_cases,test_cases) = read_input()
	
	# Create adjacency lists
	s_adj_list = create_adj_list(side_road_edges, side_road_nodes)
	m_adj_list = create_adj_list(main_road_edges, main_road_nodes)
	h_adj_list = create_adj_list(highway_edges, highway_nodes)

	# Print adjacency lists
	# print_adj_list(s_adj_list)
	# print_adj_list(m_adj_list)
	# print_adj_list(h_adj_list)

	# Run Dijkstra's algorithm on each test case
	print(dijkstra(s_adj_list, (4, 0), (3, 8)))

if __name__ == "__main__":
	main()

	

