import os
import sys
from sys import argv, exit
from scipy.sparse.csgraph import dijkstra

import CPUtimer

from data1 import instance_iterator, print_solution

def solve(instance_path, ini):
    timer = CPUtimer.CPUTimer()
    for instance in instance_iterator(instance_path):
        verticeInicial = 1
        instance_name, numVertices, numArestas, matrizAdjacencia = instance
        timer.reset()
        timer.start()
        distances, predecessors = dijkstra (matrizAdjacencia, indices=verticeInicial, return_predecessors=True, unweighted=False)
        timer.stop()
        print_solution(verticeInicial, distances, predecessors, instance_name, '1c', timer)
