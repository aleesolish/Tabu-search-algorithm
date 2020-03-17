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

def get_adjacency(edge):
    return (edge.get_node_two().get_name(), edge.get_weight())

def state_neighborhood(adjacency_list):
    return_list = []
    for adjacency in adjacency_list:
        return_list.append(get_adjacency(adjacency))
    return return_list

def set_map(cities, cities_adjacencies):
    map = []
    for city, adjacency in zip(cities, cities_adjacencies):
        dictionary = {
        'name': city.get_name(),
        'adjacencies': state_neighborhood(adjacency)
        }
        map.append(dictionary)
    return map

def first_run(map):
    start_node = map[0]
    end_node = start_node
    visiting_node = start_node
    first_solution = []
    total_first_distance = 0

    while visiting_node not in first_solution:
        min_distance = math.inf
        #for loop to determine what adjacency has the lower distance
        for adjacency in visiting_node['adjacencies']:
            #conditional to assign new minimal distance
            if adjacency[1] < min_distance and adjacency not in first_solution:
                #for loop to find the next best node
                for city in map:
                    if city['name'] == adjacency[0]:
                        next_best = city
                        distance_sum = adjacency[1]
                #print(min_distance, next_best)

        total_first_distance = total_first_distance + distance_sum
        first_solution.append(visiting_node)
        visiting_node = next_best
        print(first_solution, total_first_distance)

    """
    min_distance = visiting_node['adjacencies'][0][1]
    """

map = set_map(cities, cities_adjacencies)
#print(map)

first_run(map)
