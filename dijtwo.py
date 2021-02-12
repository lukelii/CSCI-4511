import numpy as np
from dijkstar import Graph, find_path
from datetime import datetime

start = datetime.now()

txt_path = 'p1_graph.txt'
f = open(txt_path)
data_lists = f.readlines()

Edges = []
Vertexes = []
Path = []

for data in data_lists:
    data = data.partition('#')[0]
    data = data.rstrip()
    data1 = data.strip("\n")
    data2 = data1.split(',')

    if len(data2) == 2:
        if data2[0][0] == 'S':
            Path.append(data2)
        elif data2[0][0] == 'D':
            Path.append(data2)
        else:
            Vertexes.append(data2)

    if len(data2) == 3:
        Edges.append(data2)

V = np.array(Vertexes)
V = V.astype(int)
E = np.array(Edges)
E = E.astype(int)
P = np.array(Path)

print(V)
print(E)
print(P)
print("From %s to %s" % (P[0][1], P[1][1]))

graph = Graph()
for i in range(len(E)):
    graph.add_edge(E[i][0], E[i][1], E[i][2])
print(find_path(graph, int(P[0][1]), int(P[1][1])))

print(datetime.now() - start)
