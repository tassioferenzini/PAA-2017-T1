from __future__ import print_function

import os
import sys
import CPUtimer
from collections import defaultdict

class AVL(object):

    def __init__(self, node):
        self.nodes = node
        self.left = None
        self.right = None

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        
class avltree(object):    
    
    def __init__(self):
        self.key = None
        self.nodes = set()
        self.left = None
        self.right = None
        self.edges = defaultdict(list)
        self.distances = {}
        self.height = -1
        self.balance = 0


    def insert(self, nodes):

        n = AVL(nodes)

        if not self.key:
            self.key = n
            self.key.left = avltree()
            self.key.right = avltree()
        elif nodes < self.key.nodes:
            self.key.left.insert(nodes)
        elif nodes > self.key.nodes:
            self.key.right.insert(nodes)
            
        self.rebalance()
        
    def rebalance(self):

        self.update_heights(recursive=False)
        self.update_balances(False)

        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:

                if self.key.left.balance < 0:
                    self.key.left.rotate_left()
                    self.update_heights()
                    self.update_balances()

                self.rotate_right()
                self.update_heights()
                self.update_balances()
            
            if self.balance < -1:
                
                if self.key.right.balance > 0:
                    self.key.right.rotate_right()
                    self.update_heights()
                    self.update_balances()

                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def update_heights(self, recursive=True):
        if self.key: 
            if recursive: 
                if self.key.left: 
                    self.key.left.update_heights()
                if self.key.right:
                    self.key.right.update_heights()
            
            self.height = 1 + max(self.key.left.height, self.key.right.height)
        else: 
            self.height = -1

    def update_balances(self, recursive=True):
        if self.key:
            if recursive:
                if self.key.left:
                    self.key.left.update_balances()
                if self.key.right:
                    self.key.right.update_balances()

            self.balance = self.key.left.height - self.key.right.height
        else:
            self.balance = 0 

            
    def rotate_right(self):
        new_root = self.key.left.key
        new_left_sub = new_root.right.key
        old_root = self.key

        self.key = new_root
        old_root.left.key = new_left_sub
        new_root.right.key = old_root

    def rotate_left(self):
        new_root = self.key.right.key
        new_left_sub = new_root.left.key
        old_root = self.key

        self.key = new_root
        old_root.right.key = new_left_sub
        new_root.left.key = old_root

    def delete(self, nodes):
        if self.key != None:
            if self.key.nodes == nodes:
                if not self.key.left.key and not self.key.right.key:
                    self.key = None
                elif not self.key.left.key:                
                    self.key = self.key.right.key
                elif not self.key.right.key:
                    self.key = self.key.left.key
                else:
                    successor = self.key.right.key  
                    while successor and successor.left.key:
                        successor = successor.left.key

                    if successor:
                        self.key.nodes = successor.nodes
                        self.key.right.delete(successor.nodes)

            elif nodes < self.key.nodes:
                self.key.left.delete(nodes)

            elif nodes > self.key.nodes:
                self.key.right.delete(nodes)

            self.rebalance()

    def inorder_traverse(self):
        result = []

        if not self.edges:
            return result
        
        result.extend(self.key.left.inorder_traverse())
        result.append(self.edges)
        result.extend(self.key.right.inorder_traverse())

        return result
        
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance

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
        
def parse_instanceAVL(instance_file):
    with open(instance_file) as f:
        conteudo = f.readlines()
        lines = [t.strip() for t in conteudo]

        ph = []
        countlines = 1
        for i in lines:
            if ("Section Graph" in i):
                break
            countlines += 1

        while (lines[countlines] != "End"):
            ph.append(lines[countlines].split())
            countlines += 1

        numVertices = int(ph[0][1])
        numArestas = int(ph[1][1])
 
        tree = avltree()
         
        for node in range(numVertices+1):
            tree.insert(node)

        for i in range(2, numArestas):
            vertice1 = int(ph[i][1])
            vertice2 = int(ph[i][2])
            peso = int(ph[i][3])
            tree.add_edge(vertice1,vertice2, peso) 

        return numVertices, numArestas, tree

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

def instance_iteratorAVL(instance_path):
    file_list = [f for f in os.listdir(instance_path)
    if f.endswith('.stp')]
    for filename in sorted(file_list):
        path = os.path.join(instance_path, filename)
        numVertices, numArestas, tree = parse_instanceAVL(path)
        yield (filename[0:-4], numVertices, numArestas, tree)

def print_solution(verticeInicial, distances, predecessor, instance_name, question, timer):

    if not os.path.exists("Output/Question" + str(question)):
        try:
            os.makedirs("Output/Question" + str(question))
        except OSError as exc: # Guard against race condition
                raise

    output = open((os.getcwd()+"/Output/Question"+str(question))+"/"+instance_name+".stp", "w")

    if question != '1b':    
        i = len(predecessor)-1
        caminho = []
        while (i != verticeInicial):    
            caminho.append(predecessor[i])
            i = predecessor[i]
            caminho = sorted(caminho)
    else:
        caminho = predecessor
    
    output.write("Caminho: " + str(caminho))
    
    output.write("\n\n")
    output.write("Total time: " + str( timer.get_time()) +" s")
    output.write("\nAverage time: " + str( timer.get_time("average", "seg")) + " s")
    output.write("\nLast call: " + str( timer.get_time("last")) +" s")
    output.write("\nStamp 1 of the total: " + str( timer.get_stamp("total","si"))) 
    output.write("\nStamp 2 of the total: " + str( timer.get_stamp("total","clock")))
    output.write("\nPattern that ignores zeros:")
    output.write("\n" + timer.get_stamp("total","si",True))
    output.write("\n" + timer.get_stamp("total","clock",True))
    output.write("\n\n")
