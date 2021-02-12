import numpy as np
from numpy import inf
import sys
from datetime import datetime
import networkx as nx
from networkx import astar_path

start = datetime.now()

Inf = float('inf')


def heuristic(a, b):
    global temp
    global temp2
    for x in range(10):
        for y in range(10):
            for z in range(10):
                if Square[x][y][z] == a:
                    temp2 = [x, y]
                elif Square[x][y][z] == b:
                    temp = [x, y]
    return abs(temp[0] - temp[1])*100 + abs(temp[1] - temp2[1])*100



def add_vertex(v):
    global graph
    global vertices_no
    global vertices
    if v in vertices:
        print("Vertex ", v, "already exists")
    else:
        vertices_no = vertices_no + 1
        vertices.append(v)
        if vertices_no > 1:
            for vertex in graph:
                vertex.append(0)
        temp = []
        for i in range(vertices_no):
            temp.append(0)
        graph.append(temp)


def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices

    if v1 not in vertices:
        print ("Vertex", v1, "does not exist")
    elif v2 not in vertices:
        print ("vertex", v2, "not exist.")
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e


vertices = []
vertices_no = 0
graph = []
min_index = 0

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

Square = np.zeros(1000)
Square = Square.reshape(100, 10)
for j in range(10):
    for i in range(100):
        Square[i][j] = Inf
z = 0
for x in V:
    if Square[x[1], z] == Inf:
        Square[x[1], z] = x[0]
    else:
        z = z + 1
        Square[x[1], z] = x[0]
# print(Square[0])
Square = Square.reshape(10, 10, 10)
# print(Square[0])
for i in range(len(V)):
    add_vertex((V[i][0]))
for i in range(len(E)):
    add_edge(E[i][0], E[i][1], E[i][2])

for i in range(vertices_no):
    for j in range(vertices_no):
        if graph[i][j] == 0:
            graph[i][j] = Inf
start = datetime.now()
g = nx.Graph()
for edge in range(len(E)):
    g.add_edge(E[edge,0], E[edge,1], weight = E[edge,2])
path = nx.astar_path(g,0,99,heuristic)
pl = nx.astar_path_length(g,0,99)
print (path)
print(pl)


#print(E[0])
print(datetime.now() - start)
