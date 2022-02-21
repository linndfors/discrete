"""
Module implements Prim's algorithm.
"""

import graph_generator
import random
import networkx as nx
import matplotlib.pyplot as plt
import time
from tqdm import tqdm
from networkx.algorithms import tree


def prim(G, num_of_nodes):
    """
    (dict, int) -> (list)
    Function accepts randomly generated graph and\
    number of nodes. Then the set of all nodes, set of\
    nodes through which the edges have already been drawn,\
    a list for final result (edges) and a dictionary for\
    temporarily selected nodes are created.\
    Then accepted graph is transformed into a dictionary and\
    sorted. After that a cycle of choosing edges starts and runs\
    until the set of used nodes is equal to the set of all nodes.\
    Function returns a list of edges.

    """
    graph = dict()
    for v_1, v_2, weight in G:
        edge = (v_1, v_2)
        graph[edge] = list(weight.values())[0]
    graph = dict(sorted(graph.items(), key=lambda item: item[1]))

    edges = []
    used_nodes = set()
    used_nodes.add(0)
    temporary = dict()

    while num_of_nodes != len(used_nodes):

        for key in graph.keys():
            if (key[0] in used_nodes and key[1] not in used_nodes) or (key[1] in used_nodes and key[0] not in used_nodes):
                temporary[key] = graph[key]

        key = list(temporary.keys())[0]
        edges.append(key)
        del graph[key]
        used_nodes.add(key[0])
        used_nodes.add(key[1])
        temporary = dict()
        
    return edges

# G = graph_generator.gnp_random_connected_graph(25, 1, False)
# f = nx.Graph()
# f.add_edges_from(prim(G, 25))
# nx.draw(f, with_labels=True)
# plt.show()
