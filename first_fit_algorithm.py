import time

def first_fit_algorithm(grafo):
    inicio = time.process_time()
    
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

    fim = time.process_time()

    return [cores,fim - inicio]

