from classes import *
import copy

"""
ie.
a : [('b', 100), ('c', 150), ('d', 500), ('e', 500)]
"""

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a_b = Edge(a, b, 20)
a_c = Edge(a, c, 18)
a_d = Edge(a, d, 22)
a_e = Edge(a, e, 26)

b_a = Edge(b, a, 20)
b_c = Edge(b, c, 10)
b_d = Edge(b, d, 11)
b_e = Edge(b, e, 12)

c_a = Edge(c, a, 18)
c_b = Edge(c, b, 10)
c_d = Edge(c, d, 23)
c_e = Edge(c, e, 24)

d_a = Edge(d, a, 22)
d_b = Edge(d, b, 11)
d_c = Edge(d, c, 23)
d_e = Edge(d, e, 40)

e_a = Edge(e, a, 26)
e_b = Edge(e, b, 12)
e_c = Edge(e, c, 24)
e_d = Edge(e, d, 40)

a_list = [a_b, a_c, a_d, a_e]
b_list = [b_a, b_c, b_d, b_e]
c_list = [c_a, c_b, c_d, c_e]
d_list = [d_a, d_b, d_c, d_e]
e_list = [e_a, e_b, e_c, e_d]

nodes = [a, b, c, d, e]
edges = [a_list, b_list, c_list, d_list, e_list]


#FUNCTION THAT RETURNS ADJACENCIES VALUES NAME, WEIGHT
def get_adjacency(edge):
    return (edge.get_node_two().get_name(), edge.get_weight())


#FUNCTION TO APPEND ADJACENCIES WITH NAME AND WEIGHT TO EVERY NODE ('',1)
def state_neighborhood(edges):
    return_list = []
    for edge in edges:
        return_list.append(get_adjacency(edge))
    return return_list


#FUNCTION TO CREATE A LIST OF DICTIONARIES RELATIVE TO EVERY NODE {NAME: , EDGES:}
def set_map(nodes, edges):
    map = []
    for node, edge in zip(nodes, edges):
        dictionary = {
        'node': node.get_name(),
        'edges': state_neighborhood(edge)
        }
        map.append(dictionary)
    return map


#FUNCTION FOR FIRST SOLUTION
def first_run(map):
    start_node = map[0]
    end_node = start_node
    visiting_node = start_node
    previous_node = start_node
    first_solution = []
    total_first_distance = 0

    #while end_node not in first_solution:
    while visiting_node not in first_solution:
        min_distance = 1000000
        #for loop to determine what adjacency has the lower distance
        for adjacency in visiting_node['edges']:
            #for loop to find the next best node
            for node in map:
                if node['node'] == adjacency[0]:
                    #conditional to assign new minimal distance
                    if adjacency[1] < min_distance and node not in first_solution:
                        min_distance = adjacency[1]
                        next_best = node

        first_solution.append(visiting_node)
        visiting_node = next_best
        total_first_distance = total_first_distance + min_distance

    first_solution.append(end_node)
    total_first_distance = total_first_distance - min_distance

    return first_solution, total_first_distance

#FUNCTION FOR GENERATING DOMAIN OF TABU SEARCH
def generate_tabu_search_domain(solution):
    domain = []
    for element in solution[1:-1]:
        index_one = solution.index(element)
        element_one = solution[index_one]
        for element_t in solution[1:-1]:
            index_two = solution.index(element_t)
            element_two = solution[index_two]
            if index_one == index_two:
                continue
            #element exchange
            sum = 0
            x_change = copy.deepcopy(solution)
            x_change[index_one] = element_two
            x_change[index_two] = element_one
            #lookup for next node weight
            for element in x_change[0:-1]:
                for edge in element['edges']:
                    if x_change[x_change.index(element)+1]['node'] == edge[0]:
                        sum = sum + edge[1]
                        #print(element, sum)

            x_change.append(sum)
            if x_change not in domain:
                domain.append(x_change)
    sorting_index = len(domain[0])-1
    domain.sort(key=lambda x:x[sorting_index])

    return domain

map = set_map(nodes, edges)
#print(map)
first_solution, first_total_distance = first_run(map)
#print(first_solution, first_total_distance)

domain = generate_tabu_search_domain(first_solution)
