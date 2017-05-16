import os
import sys
from sys import argv, exit
from scipy.sparse.csgraph import dijkstra

import CPUtimer

from data1 import instance_iteratorL, print_solution

def solve(instance_path):
    timer = CPUtimer.CPUTimer()
    for instance in instance_iteratorL(instance_path):
        verticeInicial = 1
        instance_name, numVertices, numArestas, listaAdjacencia = instance
        timer.reset()
        timer.start()
        distances, predecessors = dijkstra(listaAdjacencia, numVertices, verticeInicial)
        timer.stop()
        print_solution(verticeInicial, distances, predecessors, instance_name, '1a', timer)

def dijkstra(listaAdjacencia, numVertices, verticeInicial):

	distancia = [99999 for x in range(numVertices+1)]
	predecessor = [99999 for x in range(numVertices+1)]
	distancia[verticeInicial] = 0
	predecessor[verticeInicial] = 0
	flaggedVertices = [False for x in range(numVertices+1)]
	flaggedVertices[0] = True

	menor = getVerticeMenorDistancia(distancia, flaggedVertices)

	while (menor != 99999):
		flaggedVertices[menor] = True
		if (len(listaAdjacencia[menor]) > 0):
			for i in range(len(listaAdjacencia[menor])):
				vertice = listaAdjacencia[menor][i][0]
				peso = listaAdjacencia[menor][i][1]
				
				if (distancia[vertice] > (distancia[menor] + peso)):
					distancia[vertice] = distancia[menor] + peso	
					predecessor[vertice] = menor
		menor = getVerticeMenorDistancia(distancia, flaggedVertices)

	return distancia, predecessor 

def getVerticeMenorDistancia(distancia, flaggedVertices):
	
	verticesDistanciasNaoVisitados = []
	vetorIntermediario = []

	for i in range(len(flaggedVertices)):
		if (flaggedVertices[i] == False):
			vetorIntermediario.append(distancia[i])
			vetorIntermediario.append(i)
			verticesDistanciasNaoVisitados.append(vetorIntermediario)
			vetorIntermediario = []

	if (len(verticesDistanciasNaoVisitados)>0):
		menor = min(verticesDistanciasNaoVisitados)
		indiceMenor = menor[1]
		return indiceMenor
	else:
		return 99999
