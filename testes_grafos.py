import degree_of_saturation_algorithm as dsa, incidence_degree_ordering_algorithm as idoa, largest_degree_ordering_algorithm as ldoa, recursive_largest_first_algorithm as rlfa
import first_fit_algorithm as ffa, welsh_powell_algorithm as wpa, conversor_matriz as conv
import json


algoritmos = ['ffa', 'dsa', 'idoa', 'ldoa', 'rlfa', 'wpa']
grafos = ["dsjc250.5", "dsjc500.1", "dsjc500.5", "dsjc500.9", "dsjc1000.1", "dsjc1000.5",
    "dsjc1000.9", "r250.5", "r1000.1c", "r1000.5", "dsjr500.1c", "dsjr500.5",
    "le450_25c", "le450.25d", "flat300_28_0", "flat1000_50_0", "flat1000_60_0",
    "flat1000_76_0", "latin_square", "C2000.5", "C4000.5"]



def bateria_de_testes(grafo):
    resultados = {'ffa': None, 'dsa': None, 'idoa': None, 'ldoa': None, 'rlfa': None, 'wpa': None}

    resultados['ffa'] = ffa.first_fit_algorithm(grafo)
    resultados['dsa'] = dsa.degree_of_saturation_algorithm(grafo)
    resultados['idoa'] = idoa.incidence_degree_ordering_algorithm(grafo)
    resultados['ldoa'] = ldoa.largest_degree_ordering_algorithm(grafo)
    resultados['rlfa'] = rlfa.recursive_largest_first_algorithm(grafo)
    resultados['wpa'] = wpa.welsh_powell_algorithm(grafo)

    return resultados

def cores_usadas(resultado_algoritmo):
    cor_max = 0
    for cor in resultado_algoritmo.values():
        if cor > cor_max:
            cor_max = cor
    cor_max += 1
    return cor_max



def testando_tudo(grafos):
    grafos_resultados = []

    for nome_grafo in grafos:
        caminho = '/home/caio/Desktop/Geral/Python/grafos' + '/'+ nome_grafo + '.txt'
        grafo = conv.matriz_para_grafo(conv.ler_matriz(caminho))
        resultado_algoritmo = bateria_de_testes(grafo)

        for algoritmo in algoritmos:
            cor_max = cores_usadas(resultado_algoritmo[algoritmo][0])
            resultado_algoritmo.setdefault(algoritmo, []).append(cor_max)
        
        grafos_resultados.append(resultado_algoritmo)
    return grafos_resultados


aporratoda = testando_tudo(grafos)

with open('data.json', 'w') as f:
    json.dump(aporratoda, f)