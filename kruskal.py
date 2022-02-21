'''
Kruskal algorithm.
'''
import random
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import tree
import time
from tqdm import tqdm
from generate_graph import gnp_random_connected_graph

from itertools import combinations, groupby
ver_numb = 5
prob = 0.2
G = gnp_random_connected_graph(ver_numb, prob, False)

def main():
    def sort_edges_in_graph(graph, nodes):
        '''
        Return edges from the less weighted to the most
        >>> print(sort_edges_in_graph([(0, 3, {'weight': 4}), (1, 2, {'weight': 1}), (2, 3, {'weight': 0}),\
             (2, 4, {'weight': 7}), (3, 4, {'weight': 3})], [0, 1, 2, 3, 4]))
        ([(2, 3, {'weight': 0}), (1, 2, {'weight': 1}), (3, 4, {'weight': 3}), (0, 3, {'weight': 4}), (2, 4, {'weight': 7})], 5)
        '''
        sorted_edges = sorted(graph, key=lambda x: x[2]["weight"])
        number_of_vers = len(nodes)
        return sorted_edges, number_of_vers


    def create_sets(numb_of_vert):
        '''
        Create sets, which contain vert and put it in list
        >>> print(create_sets(4))
        [{0}, {1}, {2}, {3}]
        '''
        list_of_sets = []
        for set_elem in range(numb_of_vert):
            list_of_sets.append({set_elem})
        return list_of_sets

    def uniting_sets(big_set, ver1, ver2):
        '''
        Unite sets, if they have same elements
        >>> print(uniting_sets([{0}, {1}, {2}, {3}, {4}], 1, 2))
        [{0}, {3}, {4}, {1, 2}]
        '''
        counter = 0
        bad_sets = []
        right_set = set()
        for this_set in big_set:
            if counter < 2:
                if ver1 in this_set or ver2 in this_set:
                    right_set = right_set | this_set
                    counter +=1
                else:
                    bad_sets.append(this_set)
            else:
                bad_sets.append(this_set)
        list_of_right_set = [right_set]
        final_list_of_sets = bad_sets + list_of_right_set
        return final_list_of_sets

    def if_in_same(list_of_sets, ver1, ver2):
        '''
        Check if vertes in different sets or no
        >>> print(if_in_same([{0}, {2}, {4}, {1, 3}], 2, 3))
        True
        '''
        for this_set in list_of_sets:
                if ver1 in this_set or ver2 in this_set:
                    if ver1 in this_set and ver2 in this_set:
                        return False
                    return True

    def main_algorythm(edges, number_of_vers):
        '''
        The main algorythm. Return list of edges to create the smallest carcas
        '''
        spanning_tree = nx.Graph()
        count = 0
        graph_edge_list = []
        numb_of_vert = number_of_vers
        list_of_sets = create_sets(numb_of_vert)
        for pair in edges:
            if if_in_same(list_of_sets, pair[0], pair[1]):
                graph_edge_list.append(pair)
                count += 1
                if count == numb_of_vert - 1:
                    return graph_edge_list
                list_of_sets = uniting_sets(list_of_sets, pair[0], pair[1])
    

    edges, numbers_of_vers = sort_edges_in_graph(G.edges(data=True), G.nodes())
    edges_list = main_algorythm(edges, numbers_of_vers)

    #Part of code, which draw a carcass. Uncomment if you want to see a carcass.

    # f_graph = nx.Graph()

    # f_graph.add_edges_from(edges_list)

    # nx.draw(f_graph, node_color='lightgreen', 
    #             with_labels=True, 
    #             node_size=500)
    # plt.show()

if __name__ == "__main__":
    main()

    




