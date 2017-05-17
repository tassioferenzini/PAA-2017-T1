from __future__ import print_function

import os
import sys
import CPUtimer

def parse_instance(instance_file):
    
    with open(instance_file) as f:
        
        conteudo = f.readlines()
        lines = [t.strip() for t in conteudo]

        graph = []
        countlines = 1
        for i in lines:
            if ("Section Graph" in i):
                break
            countlines += 1

        while (lines[countlines] != "End"):
            graph.append(lines[countlines].split())
            countlines += 1

        numVertices = int(graph[0][1])
        numArestas = int(graph[1][1])

        matrizAdjacencia = [[0 for x in range(numVertices+1)] for x in range(numVertices+1)]

        for i in range(2, len(graph)):
            vertice1 = int(graph[i][1])
            vertice2 = int(graph[i][2])
            peso = int(graph[i][3])
            matrizAdjacencia[vertice1][vertice2] = peso 

        return numVertices, numArestas, matrizAdjacencia

def parse_instanceL(instance_file):
    with open(instance_file) as f:
        conteudo = f.readlines()
        lines = [t.strip() for t in conteudo]

        graph = []
        countlines = 1
        for i in lines:
            if ("Section Graph" in i):
                break
            countlines += 1

        while (lines[countlines] != "End"):
            graph.append(lines[countlines].split())
            countlines += 1

        numVertices = int(graph[0][1])
        numArestas = int(graph[1][1])
     
        listaAdjacencia = []
        for i in range(numVertices+1):
            listaAdjacencia.append([])

        for i in range(2, len(graph)):
            verticePeso = []
            verticePeso.append(int(graph[i][2]))
            verticePeso.append(int(graph[i][3]))
            listaAdjacencia[int(graph[i][1])].append(verticePeso)

        return numVertices, numArestas, listaAdjacencia

def instance_iterator(instance_path):
    file_list = [f for f in os.listdir(instance_path)
    if f.endswith('.stp')]
    for filename in sorted(file_list):
        path = os.path.join(instance_path, filename)
        numVertices, numArestas, matrizAdjacencia = parse_instance(path)
        yield (filename[0:-4], numVertices, numArestas, matrizAdjacencia)

def instance_iteratorL(instance_path):
    file_list = [f for f in os.listdir(instance_path)
    if f.endswith('.stp')]
    for filename in sorted(file_list):
        path = os.path.join(instance_path, filename)
        numVertices, numArestas, listaAdjacencia = parse_instanceL(path)
        yield (filename[0:-4], numVertices, numArestas, listaAdjacencia)

def print_solution(verticeInicial, distances, predecessor, instance_name, question, timer):

    if not os.path.exists("Output/Question" + str(question)):
        try:
            os.makedirs("Output/Question" + str(question))
        except OSError as exc: # Guard against race condition
                raise

    output = open((os.getcwd()+"/Output/Question"+str(question))+"/"+instance_name+".stp", "w")
    
    i = len(predecessor)-1
    caminho = []
    while (i != verticeInicial):    
        caminho.append(predecessor[i])
        i = predecessor[i]
    
    caminho = sorted(caminho)
    
    output.write("Caminho: " + str(caminho))
    
    output.write("\n\n")
    output.write("Total time: " + str( timer.get_time() ) +" s")
    output.write("\nAverage time: " + str( timer.get_time("average","micro")) + " \u00B5s")
    output.write("\nLast call: " + str( timer.get_time("last","micro") ) +" \u00B5s")
    output.write("\nStamp 1 of the total: " + str( timer.get_stamp("total","si") ) ) 
    output.write("\nStamp 2 of the total: " + str( timer.get_stamp("total","clock") ) )
    output.write("\nPattern that ignores zeros:")
    output.write("\n" + timer.get_stamp("total","si",True))
    output.write("\n" + timer.get_stamp("total","clock",True))
    output.write("\n\n")
