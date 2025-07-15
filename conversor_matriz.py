import os
import glob


def parsear_arestas(linhas):
    arestas = []
    for linha in linhas:
        partes = linha.strip().split()
        if len(partes) == 3 and partes[0].lower() == 'e':
            u, v = map(int, partes[1:])
            arestas.append((u, v))
    return arestas


def construir_matriz_adjacencia(arestas):
    if not arestas:
        return []
    max_vertice = max(max(u, v) for u, v in arestas)
    n = max_vertice + 1
    matriz = [[0] * n for _ in range(n)]
    for u, v in arestas:
        matriz[u][v] = 1
        matriz[v][u] = 1
    return matriz


def ler_matriz(caminho):

    with open(caminho, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    arestas = parsear_arestas(linhas)
    return construir_matriz_adjacencia(arestas)

def matriz_para_grafo(adj_matrix):

    grafo = {}
    for i in range(len(adj_matrix)):
        grafo[i] = []
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] == 1:
                grafo[i].append(j)
    return grafo
