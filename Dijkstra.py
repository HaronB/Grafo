import sys
 
class Graph():
    
    #Cria o grafo
    def __init__(self, vertx):
        self.V = vertx
        self.graph = [[0 for column in range(vertx)]
                      for row in range(vertx)]
 
    #Imprime as distancia
    def pSol(self, dist):
        print("Distance of vertex from source")
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
            print(u)
            sptSet[u] = True
 
            #Registra as distancia entre os pontos
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                       dist[v] = dist[u] + self.graph[u][v]
 
        self.pSol(dist)

f = Graph(6)
f.graph = [[0, 0, 6, 0, 0, 3],
           [0, 0, 0, 2, 0, 8],
           [6, 0, 0, 1, 3, 4],
           [0, 2, 1, 0, 1, 0],
           [0, 0, 3, 1, 0, 10],
           [3, 8, 4, 0, 10, 0]
           ]
 
f.dijk(5)