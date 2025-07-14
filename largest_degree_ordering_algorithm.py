import time

def largest_degree_ordering_algorithm(grafo):
    inicio = time.process_time()
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
        

    fim = time.process_time()
    return [cores,fim-inicio]

