from classes import *

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

cities = [mex, cva, qro, slp, gto]
cities_adjacencies = [mex_list, cva_list, qro_list, slp_list, gto_list]

def get_adjacency(edge):
    return (edge.get_node_two().get_name(), edge.get_weight())

def state_neighborhood(adjacency_list):
    return_list = []
    for adjacency in adjacency_list:
        return_list.append(get_adjacency(adjacency))
    return return_list

def get_map(cities, cities_adjacencies):
    map = []
    for city, adjacency in zip(cities, cities_adjacencies):
        dictionary = {
        'name': city.get_name(),
        'adjacencies': state_neighborhood(adjacency)
        }
        map.append(dictionary)
    return map

map = get_map(cities, cities_adjacencies)
print(map)
