import time

def degree_of_saturation_algorithm(grafo):
    inicio = time.process_time()
    cores = {vertice: None for vertice in grafo}
    grau = {vertice: len(grafo[vertice]) for vertice in grafo}
    cores_vizinhos = {vertice: set() for vertice in grafo}

    lista_cores = [0]
    proxima_cor = 1

    primeiro_vertice = max(grafo, key=lambda vertice: grau[vertice])
    cores[primeiro_vertice] = 0
    for vizinho in grafo[primeiro_vertice]:
        cores_vizinhos[vizinho].add(0)

    nao_coloridos = set(grafo) - {primeiro_vertice}

    while nao_coloridos:
        vertice_escolhido = max(nao_coloridos, key=lambda vertice: (len(cores_vizinhos[vertice]), grau[vertice]))
        usadas = cores_vizinhos[vertice_escolhido]
        cor = next((c for c in lista_cores if c not in usadas), None)
        if cor is None:
            cor = proxima_cor
            lista_cores.append(cor)
            proxima_cor += 1
        cores[vertice_escolhido] = cor
        for vizinho in grafo[vertice_escolhido]:
            cores_vizinhos[vizinho].add(cor)
        nao_coloridos.remove(vertice_escolhido)

    fim = time.process_time()
    return [cores, fim - inicio]
