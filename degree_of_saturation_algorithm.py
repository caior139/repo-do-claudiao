def matriz_para_grafo(adj_matrix):
    grafo = {}
    for i in range(len(adj_matrix)):
        grafo[i] = []
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] == 1:
                grafo[i].append(j)
    return grafo

def degree_of_saturation_algorithm(matriz_adj):

    grafo = matriz_para_grafo(matriz_adj)
    cores = {}
    grau = {}
    lista_cores = [0]
    proxima_cor = 1

    for vertice in grafo:
        cores[vertice] = None
        grau[vertice] = len(grafo[vertice])

    lista_grau = []
    for item in grau.items():
        lista_grau.append(item)
    lista_grau.sort(key=lambda x: x[1], reverse=True)

    primeiro_vertice = lista_grau[0][0]
    cores[primeiro_vertice] = 0

    while True:
        vizinhos_coloridos = {}
        for vertice in grafo:
            if cores[vertice] is not None:
                continue
            count = 0
            for cor in lista_cores:
                for vizinho in grafo[vertice]:
                    if cores[vizinho] == cor:
                        count += 1
                        break
            vizinhos_coloridos[vertice] = count

        if not vizinhos_coloridos:
            break

        max_saturacao = -1
        vertice_para_colorir = None
        for vertice in vizinhos_coloridos:
            sat = vizinhos_coloridos[vertice]
            if (vertice_para_colorir is None
                or sat > max_saturacao
                or (sat == max_saturacao and grau[vertice] > grau[vertice_para_colorir])
            ):
                max_saturacao = sat
                vertice_para_colorir = vertice

        cor_escolhida = -1
        for cor in lista_cores:
            pode_usar = True
            for vizinho in grafo[vertice_para_colorir]:
                if cores[vizinho] == cor:
                    pode_usar = False
                    break
            if pode_usar:
                cor_escolhida = cor
                break

        if cor_escolhida == -1:
            cor_escolhida = proxima_cor
            lista_cores.append(proxima_cor)
            proxima_cor += 1

        cores[vertice_para_colorir] = cor_escolhida
    return cores

matriz = [
[0,1,1,0,0,0,0],
[1,0,1,0,0,0,1],
[1,1,0,1,1,0,0],
[0,0,1,0,0,1,0],
[0,0,1,0,0,1,1],
[0,0,0,1,1,0,0],
[0,1,0,0,1,0,0]]
    
print(degree_of_saturation_algorithm(matriz))