import networkx as nx

def createGraph():
    name = input("Enter Name for Graph: ")
    print("Input file:")
    V = int(input())
    Graph = nx.DiGraph()
    for i in range(V):
        Graph.add_node((i+1))
    for i in range(V):
        line = input().split()
        numE = int(line[0])
        for j in range(numE):
            Graph.add_edge(i+1,line[j+1])
    print("All Lines pasted.")

    G = nx.nx_pydot.to_pydot(Graph)
    G.write_png(f"{name}.png")
    return Graph

createGraph()