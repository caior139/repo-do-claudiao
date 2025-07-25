import time

def incidence_degree_ordering_algorithm(grafo):
    inicio = time.process_time()

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
            for vizinho in grafo[vertice]:
                if cores[vizinho] is not None:
                    count += 1
            vizinhos_coloridos[vertice] = count

      
        if len(vizinhos_coloridos) == 0:
            break

 
        max_incidente = -1
        vertice_para_colorir = None
        for vertice in vizinhos_coloridos:
            count = vizinhos_coloridos[vertice]
            if (vertice_para_colorir is None
            or count > max_incidente
            or (count == max_incidente and grau[vertice] > grau[vertice_para_colorir])):
                max_incidente = count
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


    fim = time.process_time()

    return [cores,fim-inicio]

