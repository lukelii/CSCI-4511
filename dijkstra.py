import numpy as np
from numpy import inf
import sys
from datetime import datetime
start = datetime.now()

Inf = float('inf')


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist,goal):
        print ("Vertex Distance from Source")
        for node in range(self.V):
            if node == goal:
                print (node, "\t", dist[node])

    def minDistance(self, dist, sptSet):
        global min_index
        min = sys.maxsize

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src, goal):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist, goal)

    def add_vertex(self, v):
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

    def add_edge(self, v1, v2, e):
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
g = Graph(100)

Square = np.zeros(1000)
Square = Square.reshape(100, 10)
for i in range(100):    
    for j in range(10):        
        Square[i][j] = Inf
z=0
for x in V:    
    if Square[x[1], z] == Inf:        
        Square[x[1], z] = x[0]    
    else:        
        z =z + 1        
        Square[x[1],z] = x[0]
print(Square[0])
Square = Square.reshape(10, 10, 10)



for i in range(len(V)):
    g.add_vertex((V[i][0]))
for i in range(len(E)):
    g.add_edge(E[i][0], E[i][1], E[i][2])

for i in range(vertices_no):
    for j in range(vertices_no):
        if graph[i][j] == 0:
            graph[i][j] = Inf

g.graph = graph
g.dijkstra(0,99)
#print(V)
print( datetime.now()-start )
