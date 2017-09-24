from collections import defaultdict
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

	def __str__(self):
		s = ''
		for from_node, to_nodes in self.edges.items():
			s += from_node + ':\n'
			for node in to_nodes:
				s += '   - ' + node + '\n'
		return s[:-1]

	def view(self):
		graph = graphviz.Graph('graph')
		for node in self.nodes:
			graph.node(node, node)
		for head_node in self.nodes:
			for tail_node in self.edges[head_node]:
				graph.edge(head_node, tail_node, concentrate = 'True')
		graph.view()

if __name__ == '__main__':
	graph = Graph()
	graph.add_node('a','b','c')
	graph.add_edge(('a','b'), ('b','c'), ('c','a'))
	print(graph)
	graph.view()

