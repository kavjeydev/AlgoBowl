import networkx as nx
import fileinput

def createGraphText():
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

def createGraphFile():
    name = input("Enter Name of File to Read From w/o Filetype: ")
    file = fileinput.input(f"{name}.txt")
    V = int(file[0])
    Graph = nx.DiGraph()
    for i in range(V):
        Graph.add_node((i+1))
    for i in range(V):
        line = file[i+1].split()
        numE = int(line[0])
        for j in range(numE):
            Graph.add_edge(i+1,line[j+1])

    G = nx.nx_pydot.to_pydot(Graph)
    G.write_png(f"{name}.png")
    return Graph

def createGraph():
    choice = int(input("Text(0) or File(1): "))
    if choice == 0:
        return createGraphText()
    elif choice == 1:
        return createGraphFile()
    else:
        print("Invalid Choice, Try Again!")
        return createGraph()