import sys
import networkx as nx
import matplotlib.pyplot as plt
import time
import random
import csv

#Gera a imagem do grafo
def Grafico(G):

    dict([((source,sink), data['weight']) for source, sink,data in G.edges(data=True)])

    pos = nx.spring_layout(G)

    plt.figure()
    nx.draw_networkx(G, pos, with_labels= True, node_size=10)
    nx.draw_networkx_nodes(G, pos)
    plt.show()

#Coverte o grafico gerado automaticamente em uma matrix para ser usada na class
def CovertMatrix(n, G):
    matrix = [[0 for x in range(n)] for y in range(n)]
    for source, sink, data in G.edges(data=True):
        matrix[source][sink] = data['weight']
    return matrix
    
class Graph():
    
    #Cria o grafo
    def __init__(self, vertx):
        self.V = vertx
        self.graph = [[0 for column in range(vertx)]
                      for row in range(vertx)]
 
    #Imprime as distancia
    def pSol(self, dist):
        print("Distancia da origem")
        for node in range(self.V):
            print(node, "t", dist[node])
 
    #Menor distancia
    def minDistance(self, dist, sptSet):
 
        #Inicia um variavel com um valor muito alto 
        min = sys.maxsize
        #Compara se o resultado é o menor encontrado
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    #Algoritmo Dijk
    def dijk(self, source):
        
        #Cria uma lista com um valor muito alto do tamanho do numero de vertices
        dist = [sys.maxsize] * self.V
        #Set a distancia do ponto inicial como 0
        dist[source] = 0
       
        #Inicia a variavle para ver se foi visitado
        sptSet = [False] * self.V
 
        #For para cada vertice
        for cout in range(self.V):
            
            
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
 
            #Registra as distancia entre os pontos
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                       dist[v] = dist[u] + self.graph[u][v]
 
        self.pSol(dist)

#numero de vertices
n = 100

#chance de ter uma aresta
p = 0.1

G1 = nx.gnp_random_graph(n, p, directed=True)
for (u, v) in G1.edges():
    G1.edges[u,v]['weight'] = random.randint(1,10)
    
G2 = nx.gnp_random_graph(n, p, directed=True)
for (u, v) in G2.edges():
    G2.edges[u,v]['weight'] = random.randint(1,10)
    
G3 = nx.gnp_random_graph(n, p, directed=True)
for (u, v) in G3.edges():
    G3.edges[u,v]['weight'] = random.randint(1,10)
    
#Tempo inicio
inicio = time.time()

#Cria um objeto class grafo e os vértices
f1 = Graph(n)

#Cria as arestas
f1.graph = CovertMatrix(n, G1)

#Exibe o Grafo
Grafico(G1)

#Dijkstra
f1.dijk(3)

#Tempo Fim
fim = time.time()
print("\nTempo pecorrido Grafo1: {0}".format(fim-inicio))

#Escreve um arquivo com a matrix do grafo
with open ('Grafo1.CSV', mode='w', newline='') as csv_file:
    dados_csv = csv.writer(csv_file, delimiter = ';') 
    dados_csv.writerow([i for i in range(100)])
    for i in CovertMatrix(n, G1):
        dados_csv.writerow(i)

#Tempo inicio
inicio = time.time()

#Cria um objeto class grafo e os vértices
f2 = Graph(n)

#Cria as arestas
f2.graph = CovertMatrix(n, G2)

#Exibe o Grafo
Grafico(G2)

#Dijkstra
f2.dijk(9)

#Tempo Fim
fim = time.time()
print("\nTempo pecorrido Grafo2: {0}".format(fim-inicio))

#Escreve um arquivo com a matrix do grafo
with open ('Grafo2.CSV', mode='w', newline='') as csv_file:
    dados_csv = csv.writer(csv_file, delimiter = ';') 
    dados_csv.writerow([i for i in range(100)])
    for i in CovertMatrix(n, G2):
        dados_csv.writerow(i)

#Tempo inicio
inicio = time.time()

#Cria um objeto class grafo e os vértices
f3 = Graph(n)

#Cria as arestas
f3.graph = CovertMatrix(n, G3)

#Exibe o Grafo
Grafico(G3)

#Dijkstra
f3.dijk(10)

#Tempo Fim
fim = time.time()
print("\nTempo pecorrido Grafo3: {0}".format(fim-inicio))

#Escreve um arquivo com a matrix do grafo
with open ('Grafo3.CSV', mode='w', newline='') as csv_file:
    dados_csv = csv.writer(csv_file, delimiter = ';') 
    dados_csv.writerow([i for i in range(100)])
    for i in CovertMatrix(n, G3):
        dados_csv.writerow(i)

