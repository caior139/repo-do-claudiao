import time

def recursive_largest_first_algorithm(grafo):
    inicio = time.process_time()
    cor = 0
    cores = {}
    grau = {}

    for vertice in grafo:
        cores[vertice] = None
        grau[vertice] = len(grafo[vertice])

    lista_grau = []
    for item in grau.items():
        lista_grau.append(item)
    lista_grau.sort(key=lambda x: x[1], reverse=True)

    while lista_grau:
        vertice_raiz = lista_grau[0][0]
        cores[vertice_raiz] = cor
        vizinhos_vertice = set(grafo[vertice_raiz])

        nao_vizinhos = set()
        for vertice in grafo:
            if cores[vertice] is None and vertice not in vizinhos_vertice and vertice != vertice_raiz:
                nao_vizinhos.add(vertice)

        while nao_vizinhos:
            contagens = {}
            for vertice in nao_vizinhos:
                c = 0
                for vizinho in grafo[vertice]:
                    if vizinho in vizinhos_vertice:
                        c += 1
                contagens[vertice] = c

            if not contagens:
                break

            max_contagem = -1
            candidatos = []
            for vertice, contagem in contagens.items():
                if contagem > max_contagem:
                    max_contagem = contagem
                    candidatos = [vertice]
                elif contagem == max_contagem:
                    candidatos.append(vertice)

            vertice_a_ser_pintado = None
            max_grau = -1
            for candidato in candidatos:
                if grau[candidato] > max_grau:
                    max_grau = grau[candidato]
                    vertice_a_ser_pintado = candidato

            if vertice_a_ser_pintado is None:
                break

            cores[vertice_a_ser_pintado] = cor
            novos_vizinhos = set(grafo[vertice_a_ser_pintado]) - vizinhos_vertice
            vizinhos_vertice.update(novos_vizinhos)

            nao_vizinhos.discard(vertice_a_ser_pintado)
            for vizinho in novos_vizinhos:
                nao_vizinhos.discard(vizinho)

        nova_lista_grau = []
        for vertice, g in lista_grau:
            if cores[vertice] is None:
                nova_lista_grau.append((vertice, g))
        lista_grau = nova_lista_grau

        cor += 1

    fim = time.process_time()
    return [cores, fim - inicio]