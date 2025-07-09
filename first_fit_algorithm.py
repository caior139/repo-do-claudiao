def matriz_para_grafo(adj_matrix):
    grafo = {}
    for i in range(len(adj_matrix)):
        grafo[i] = []
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] == 1:
                grafo[i].append(j)
    return grafo

def first_fit_algorithm(matriz_adj):
    grafo = matriz_para_grafo(matriz_adj)
    
    cores = {}
    for vertice in grafo:
        cores[vertice] = None

    for vertice in grafo:
        cores_vizinhos = set()
        for vizinho in grafo[vertice]:
            if cores[vizinho] is not None:
                cores_vizinhos.add(cores[vizinho])
        
        cor = 0
        while cor in cores_vizinhos:
            cor += 1

        cores[vertice] = cor

    return cores
