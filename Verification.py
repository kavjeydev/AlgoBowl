import createGraph
import networkx as nx

def verifyOutput(graph):
    G = graph
    numToDelete = int(input())
    V = input().split()
    for i in range(numToDelete):
        G.remove_node(V[i])
    return nx.is_directed_acyclic_graph(G)

G = createGraph()
print(verifyOutput(G))