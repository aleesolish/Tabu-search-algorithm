from classes import *
import math

"""
mx : [("cva", 100), ("qro", 150), ("slp", 500), ("acpco", 500)]
"""

mex = Node('mex')
cva = Node('cva')
qro = Node('qro')
slp = Node('slp')
gto = Node('gto')

mex_cva = Edge(mex, cva, 100)
mex_qro = Edge(mex, qro, 200)

cva_mex = Edge(cva, mex, 100)

qro_mex = Edge(qro, mex, 200)
qro_gto = Edge(qro, gto, 100)
qro_slp = Edge(qro, slp, 250)

slp_qro = Edge(slp, qro, 250)
slp_gto = Edge(slp, gto, 150)

gto_qro = Edge(gto, qro, 100)
gto_slp = Edge(gto, slp, 150)

mex_list = [mex_cva, mex_qro]
cva_list = [cva_mex]
qro_list = [qro_mex, qro_slp, qro_gto]
slp_list = [slp_qro, slp_gto]
gto_list = [gto_qro, gto_slp]

cities = [cva, mex, qro, slp, gto]
cities_adjacencies = [cva_list, mex_list, qro_list, slp_list, gto_list]


#FUNCTION THAT RETURNS ADJACENCIES VALUES NAME, WEIGHT
def get_adjacency(edge):
    return (edge.get_node_two().get_name(), edge.get_weight())


#FUNCTION TO APPEND ADJACENCIES WITH NAME AND WEIGHT TO EVERY CITY ('',1)
def state_neighborhood(adjacency_list):
    return_list = []
    for adjacency in adjacency_list:
        return_list.append(get_adjacency(adjacency))
    return return_list


#FUNCTION TO CREATE A LIST OF DICTIONARIES RELATIVE TO EVERY CITY {NAME: , ADJACENCIES:}
def set_map(cities, cities_adjacencies):
    map = []
    for city, adjacency in zip(cities, cities_adjacencies):
        dictionary = {
        'name': city.get_name(),
        'adjacencies': state_neighborhood(adjacency)
        }
        map.append(dictionary)
    return map


#FUNCTION FOR FIRST SOLUTION
def first_run(map):
    start_node = map[0]
    end_node = map[-1]
    visiting_node = start_node
    previous_node = start_node
    first_solution = []
    total_first_distance = 0

    while visiting_node not in first_solution:
        min_distance = math.inf
        #for loop to determine what adjacency has the lower distance
        for adjacency in visiting_node['adjacencies']:
            #conditional to assign new minimal distance
            if adjacency[1] < min_distance and adjacency is not previous_node: #not in first_solution:
                #for loop to find the next best node
                for city in map:
                    if city['name'] == adjacency[0]:
                        next_best = city
                        distance_sum = adjacency[1]


        total_first_distance = total_first_distance + distance_sum
        first_solution.append(visiting_node)
        previous_node = visiting_node
        visiting_node = next_best

    return first_solution, total_first_distance



map = set_map(cities, cities_adjacencies)
first_solution, first_total_distance = first_run(map)
print(first_solution, first_total_distance)
