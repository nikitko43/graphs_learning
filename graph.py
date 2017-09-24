from collections import defaultdict
from random import randint, choice
import graphviz

class Graph:
	def __init__(self):
		self.nodes = set()
		self.edges = defaultdict(list)

	def add_node(self, *nodes):
		for node in nodes:
			self.nodes.add(node)

	def add_edge(self, *edges):
		for (from_node, to_node) in edges:
			self.edges[from_node].append(to_node)
			self.edges[to_node].append(from_node)

	def __str__(self):
		s = ''
		for from_node in self.nodes:
			s += from_node + ':\n'
			for node in self.edges[from_node]:
				s += '   - ' + node + '\n'
		return s[:-1]

	def view(self):
		graph = graphviz.Graph('graph')
		drew_nodes = []
		for node in self.nodes:
			graph.node(node, node)
		for from_node in self.nodes:
			for to_node in self.edges[from_node]:
				if to_node not in drew_nodes:
					graph.edge(from_node, to_node, concentrate = 'True')
			drew_nodes.append(from_node)
		graph.view()
	
	def random(self, amount_of_nodes = 5, amount_of_edges = 1):
		self.__init__()
		while len(self.nodes) < amount_of_nodes:
			self.nodes.add(chr(randint(97,122)) + chr(randint(97,122)))

		nodes_not_connected = set(self.nodes)
		current_node = choice(tuple(self.nodes))
		nodes_not_connected.discard(current_node)

		while nodes_not_connected:
			new_node = choice(tuple(nodes_not_connected))
			self.add_edge((current_node, new_node))
			current_node = new_node
			nodes_not_connected.discard(new_node)

		nodes_not_visited = set(self.nodes)
		while nodes_not_visited:
			current_node = choice(tuple(nodes_not_visited))
			while len(self.edges[current_node]) < amount_of_edges:
				nodes_to_connect = self.nodes - set([current_node]) - set(self.edges[current_node])
				nodes_to_connect -= set([node for node in self.nodes if current_node in self.edges[node]])
				if len(nodes_to_connect) == 0:
					break
				choiced_node = choice(tuple(nodes_to_connect))
				self.add_edge((current_node, choiced_node))
			nodes_not_visited.discard(current_node)

		def find_path(self, from_node, to_node):
			pass

if __name__ == '__main__':
	graph = Graph()
	graph.add_node('a','b','c')
	graph.add_edge(('a','b'), ('b','c'), ('c','a'))
	graph.random(15,5)
	print(graph)
	graph.view()

