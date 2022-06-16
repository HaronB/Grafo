class Graph:

    #Cria o grafo
    def __init__(self, vertices):

        self.M = vertices   # Total number of vertices in the graph

        self.graph = []     # Array of edges



    # Adiciona arestas 

    def add_edge(self, a, b, c):

        self.graph.append([a, b, c])



    # Imprime solução 

    def print_solution(self, distance):

        print("Vertex Distance from Source")

        for k in range(self.M):

            print("{0}\t\t{1}".format(k, distance[k]))


    #Algoritmo Bellman_ford
    def bellman_ford(self, src):

        
        #marca a ddistancia como inf
        distance = [float("Inf")] * self.M

        #Set a distancia do ponto inicial como 0
        distance[src] = 0


        
        for _ in range(self.M - 1):
            
            #Distancia entre os vertices
            for a, b, c in self.graph:

                if distance[a] != float("Inf") and distance[a] + c < distance[b]:

                    distance[b] = distance[a] + c


        #Verifica se não tem um loop negativo
        for a, b, c in self.graph:

            if distance[a] != float("Inf") and distance[a] + c < distance[b]:

                print("Graph contains negative weight cycle")

                return



        self.print_solution(distance)



g = Graph(5)

g.add_edge(0, 2, 6)
g.add_edge(0, 3, -4)

g.add_edge(1, 0, -2)

g.add_edge(2, 1, -3)
g.add_edge(2, 3, 3)

g.add_edge(3, 1, 7)

g.add_edge(4, 0, 5)
g.add_edge(4, 2, 7)


g.bellman_ford(4)