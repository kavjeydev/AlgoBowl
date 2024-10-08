import networkx as nx
import fileinput


file = open("C3PO/input_group784.txt", "r")
file_content = file.read().split("\n")

num_courses_required = int(file_content[0]) # first like of input file is # courses required

tuples = []

for i in range(1, num_courses_required + 1):
    reqs = file_content[i].split(" ")[1:]
    for j in range(len(reqs)):
        tuples.append((i, int(reqs[j])))

#print(tuples)
#edges = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 0), (2, 1), (2, 2)]
G = nx.DiGraph(tuples)
print(tuples)

cycles = ((nx.simple_cycles(G)))

count_dict = {}
i = 1
for cycle in cycles:
    for j in range(len(cycle)):
        if cycle[j] in count_dict:
            count_dict[cycle[j]] += 1
        else:
            count_dict[cycle[j]] = 1

print(count_dict)
