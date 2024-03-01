import createGraph
import networkx as nx

def readFile(filename):
    
    file = open(filename, "r")
    file_content = file.read().split("\n")

    num_removed = int(file_content[0])
    nodes_removed = (file_content[1].split(" "))

    return num_removed, nodes_removed

def createGraph():
    file = open("AlgoBowl/input_group791.txt", "r")
    file_content = file.read().split("\n")

    num_courses_required = int(file_content[0]) # first like of input file is # courses required

    tuples = []

    for i in range(1, num_courses_required + 1):
        reqs = file_content[i].split(" ")[1:]
        for j in range(len(reqs)):
            tuples.append((i, int(reqs[j])))

    G = nx.DiGraph(tuples)

    return G

for i in range(721, 798):
    G = createGraph()
    if i != 790:
        num_removed, nodes_removed = readFile("AlgoBowl/outputs/output_from_" + str(i) + "_to_791.txt")
    for j in range(1, num_removed + 1):
        G.remove_node(int(nodes_removed[j - 1]))
    print("AlgoBowl/outputs/output_from_" + str(i) + "_to_791.txt", nx.is_directed_acyclic_graph(G))