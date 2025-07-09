def matriz_para_grafo(adj_matrix):
    grafo = {}
    for i in range(len(adj_matrix)):
        grafo[i] = []
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] == 1:
                grafo[i].append(j)
    return grafo

def welsh_powell_algorithm(grafo):
    cores = {}
    grau = {}

    for vertice in grafo:
        cores[vertice] = None
        grau[vertice] = len(grafo[vertice])


    vertices_ordenados = sorted(grau.items(), key=lambda x: x[1], reverse=True)

    cor = 0
    while True:
        for item in vertices_ordenados:
            vertice = item[0]
            
            if cores[vertice] is None:
                pode_colorir = True
                for vizinho in grafo[vertice]:
                    if cores[vizinho] == cor:
                        pode_colorir = False
                        break
                if pode_colorir:
                    cores[vertice] = cor


        todos_coloridos = True
        for vertice in cores:
            if cores[vertice] is None:
                todos_coloridos = False
                break

        if todos_coloridos:
            break

        cor += 1

    return cores

