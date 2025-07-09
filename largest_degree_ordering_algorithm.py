def matriz_para_grafo(adj_matrix):
    grafo = {}
    for i in range(len(adj_matrix)):
        grafo[i] = []
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] == 1:
                grafo[i].append(j)
    return grafo


def largest_degree_ordering_algorithm(matriz_adj):
    grafo = matriz_para_grafo(matriz_adj)
    
    cores = {}
    grau = {}

    for vertice in grafo:
        cores[vertice] = None
        grau[vertice] = len(grafo[vertice])


    grau = sorted(grau.items(), key=lambda x: x[1], reverse=True)


    for i in grau:
        cores_vizinhos = set()
        for vizinho in grafo[i[0]]:
            if cores[vizinho] is not None:
                cores_vizinhos.add(cores[vizinho])
        cor = 0
        while cor in cores_vizinhos:
            cor += 1

        cores[i[0]] = cor
        


    return cores

