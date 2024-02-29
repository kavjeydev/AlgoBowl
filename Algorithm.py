import createGraph as cg
import networkx as nx
import time
import os

def checkRepeats(c, l):
    for cycle in c:
        check = False
        for node in cycle:
            if node in l:
                check = True
        if check == False:
            return True
    return False


def deleteNodes(G):
    cycles = nx.simple_cycles(G)
    c2 = []
    d = {}
    for i in G.nodes:
        d[i] = 0
    for cycle in cycles:
        c2.append(cycle)
        for i in cycle:
            d[i] += 1
    list = []

    while(checkRepeats(c2, list)):
        nodeToDelete = max(d, key=d.get)
        print(nodeToDelete) #Progress Check
        list.append(nodeToDelete)
        for cycle in c2:
            if nodeToDelete in cycle:
                for i in cycle:
                    d[i] = d.get(i)-1

    return list

def Algorithm():
    start = time.time()
    G = cg.createGraph()
    end = time.time()
    print(f"Time to Create Graph was {end-start} seconds.")

    run_start = time.time()
    count = 0
    list = ""
    cycleCount = 0
    while(nx.is_directed_acyclic_graph(G) == False):
        cycleCount+=1
        cycle_start = time.time()
        listToDelete = deleteNodes(G)
        cycle_end = time.time()
        print(f"Time to Find Nodes to Delete in Cycle {cycleCount}: {cycle_end-cycle_start} s")
        for i in range(len(listToDelete)):
            list += f"{listToDelete[i]} "
        G.remove_nodes_from(listToDelete)
        count += len(listToDelete)
        print(count) # Progress Check

    print(count)
    print(list)
    run_end = time.time()
    print(f"Total Time to Find Solution was {run_end-run_start} seconds.")

def autoAlgorithm(folder):
    files = os.listdir(folder)
    for i in files:
        start = time.time()
        G = cg.createGraphFile(f"{folder}/{i}")
        end = time.time()
        print(f"Time to Create Graph was {end-start} seconds.")

        run_start = time.time()
        count = 0
        list = ""
        cycleCount = 0
        while(nx.is_directed_acyclic_graph(G) == False):
            cycleCount+=1
            cycle_start = time.time()
            listToDelete = deleteNodes(G)
            cycle_end = time.time()
            print(f"Time to Find Nodes to Delete in Cycle {cycleCount}: {cycle_end-cycle_start} s")
            for j in range(len(listToDelete)):
                list += f"{listToDelete[j]} "
            G.remove_nodes_from(listToDelete)
            count += len(listToDelete)
            print(count) # Progress Check

        output = f"/outputs/{i[:-4]}_output.txt"
        if os.path.isfile(output):
            os.remove(output)
        f = open(output, "x")
        f.write(f"{count}\n{list}")
        run_end = time.time()
        print(f"Total Time to Find Solution was {run_end-run_start} seconds.")