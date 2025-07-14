import time

def welsh_powell_algorithm(grafo):
    inicio = time.process_time()
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
                pode_colorar = True
                for vizinho in grafo[vertice]:
                    if cores[vizinho] == cor:
                        pode_colorar = False
                        break
                if pode_colorar:
                    cores[vertice] = cor


        todos_coloridos = True
        for vertice in cores:
            if cores[vertice] is None:
                todos_coloridos = False
                break

        if todos_coloridos:
            break

        cor += 1
    
    fim = time.process_time()
    return [cores, fim - inicio]

