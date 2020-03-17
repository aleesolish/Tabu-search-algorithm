from classes import *

"""
mx : [("cva", 100), ("qro", 150), ("slp", 500), ("acpco", 500)]
"""

mex = Node('mex')
cva = Node('cva')
qro = Node('qro')
slp = Node('slp')

mex_cva = Edge(mex, cva, 100)
mex_qro = Edge(mex, qro, 200)

cva_mex = Edge(cva, mex, 100)

qro_mex = Edge(qro, mex, 200)
qro_slp = Edge(qro, slp, 250)

slp_qro = Edge(slp, qro, 250)

mex_list = [mex_cva, mex_qro]
cva_list = [cva_mex]
qro_list = [qro_mex, qro_slp]
slp_list = [slp_qro]

cities = [mex_list, cva_list, qro_list, slp_list]

def get_adjacency(edge):
    return (edge.get_node_two().get_name(), edge.get_weight())

def state_neighborhood(adjacency_list):
    return_list = []
    for adjacency in adjacency_list:
        return_list.append(get_adjacency(adjacency))
    return return_list

for city in cities:
    print(state_neighborhood(city))
