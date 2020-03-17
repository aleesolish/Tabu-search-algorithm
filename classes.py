"""
class Node
attributes: name which in this case represents the name of a city ie. mex, cva, qro
"""

class Node:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

"""
class edge
attributes: node_one, node_two and weight which respectively represent first node of an adjacency, second node of an adjacency and the weight of said adjacency
"""

class Edge:

    def __init__(self, node_one, node_two, weight):
        self.node_one = node_one
        self.node_two = node_two
        self.weight = weight

    def get_node_one(self):
        return self.node_one

    def get_node_two(self):
        return self.node_two

    def get_weight(self):
        return self.weight
