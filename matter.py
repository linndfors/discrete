import random
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import tree
import time
from tqdm import tqdm

from itertools import combinations, groupby

def gnp_random_connected_graph(num_of_nodes: int,
                               completeness: int,
                               draw: bool = False) -> list[tuple[int, int]]:
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi 
    graph, but enforcing that the resulting graph is conneted
    """

    edges = combinations(range(num_of_nodes), 2)
    G = nx.Graph()
    G.add_nodes_from(range(num_of_nodes))
    
    for _, node_edges in groupby(edges, key = lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < completeness:
                G.add_edge(*e)
                
    for (u,v,w) in G.edges(data=True):
        w['weight'] = random.randint(0,10)
    if draw: 
        plt.figure(figsize=(10,6))
        nx.draw(G, node_color='lightblue', 
            with_labels=True, 
            node_size=500)
    
    return G

G = gnp_random_connected_graph(300, 1, False)
# print(G)


def sort_edges_in_graph(graph):
    '''
    Return edges from the less weighted to the most
    '''
    edges_collection = {}
    vers = set()
    for v_1, v_2, weight in graph:
        vers.add(v_1)
        vers.add(v_2)
        # w_type= type(weight)
        # print(w_type)
        edge = (v_1, v_2)
        edges_collection[edge] = weight['weight']
        sorted_edges = dict(sorted(edges_collection.items(), key=lambda t: t[1]))
    number_of_vers = max(vers) + 1
    return sorted_edges, vers, number_of_vers

def main_algorith(edges, list_of_vers):
    count = 0
    edges_list = []
    edge_colection = []
    for pair in edges.items():
        add = False
        if len(edges_list) == 0:
            weight = pair[1]
            count += weight
            edges_list.append(set(pair[0]))
            edge_colection.append(pair[0])
        # if len(edges_list[0]) == len(list_of_vers):
        #     return count, edge_colection, edges_list
        else:
            light_set_1 = None
            light_set_2 = None
            for ind, set_set in enumerate(edges_list):
                if pair[0][0] in set_set:
                    light_set_1 = edges_list[ind]
                if pair[0][1] in set_set:
                    light_set_2 = edges_list[ind]
                if light_set_1 and light_set_2:
                    if light_set_2 != light_set_1:
                        unit_list = light_set_1 | light_set_2
                        edges_list.remove(light_set_2)
                        edges_list.remove(light_set_1)
                        edges_list.append(unit_list)
                        # if len(edges_list) == 7:
                        edge_colection.append(pair[0])
                        weight = pair[1]
                        count += weight
                        # edges_list = [edges_list]
            counter = 0
            for element in edges_list:
                if pair[0][0] in element:
                    if pair[0][1] in element:
                        add = True
                elif pair[0][0] not in element:
                    if pair[0][1] not in element:
                        # edges_list.append(set(pair[0]))
                        counter +=1
                        if counter == len(edges_list):
                            edges_list.append(set(pair[0]))
                            weight = pair[1]
                            count += weight
                            edge_colection.append(pair[0])
                    elif pair[0][1] in element:
                        if add != True:
                            edges_list[0].add(pair[0][0])
                            add = True
                            weight = pair[1]
                            count += weight
                            edge_colection.append(pair[0])
            if pair[0][0] in element:
                if pair[0][1] not in element:
                    if add != True:
                        edges_list[0].add(pair[0][1])
                        add = True
                        weight = pair[1]
                        count += weight
                        edge_colection.append(pair[0])
        if len(edges_list[0]) == len(list_of_vers):
                return count, edge_colection, edges_list 

mstk = list(tree.minimum_spanning_tree(G, algorithm="kruskal"))
edges, list_of_vers, number_of_vers = sort_edges_in_graph(G.edges(data = True))
# print('Number:', number_of_vers)
# print('All vers:', list_of_vers)
# print('Edges:', edges)
weight, edge_colection, edges_list = main_algorith(edges, list_of_vers)
# print('edge colection:', edge_colection)
# print('weight:', weight)
# print('edge list:', edges_list)
f_graph = nx.Graph()

f_graph.add_edges_from(edge_colection)

nx.draw(f_graph, node_color='lightgreen', 
            with_labels=True, 
            node_size=500)
plt.show()

NUM_OF_ITERATIONS = 1000

time_taken = 0
for i in tqdm(range(NUM_OF_ITERATIONS)):
    
    # note that we should not measure time of graph creation
    G = gnp_random_connected_graph(100, 0.1, False)
    
    start = time.time()
    tree.minimum_spanning_tree(G, algorithm="kruskal")
    end = time.time()
    
    time_taken += end - start
    
print(time_taken / NUM_OF_ITERATIONS)
