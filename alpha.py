import os
import math
import sys
import CPUtimer

from sys import argv, exit


class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.predecessor = None
        self.distance = 999999999999999999999999999999999999

    def __repr__(self):
        return str(self.key)

    def set_predecessor(self, predecessor):
        self.predecessor = predecessor

    def get_predecessor(self):
        return self.predecessor

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance


class ScapeGoatTree():
    def __init__(self, a):
        self.a = a
        self.size = 0
        self.max_size = 0
        self.root = None

    # Return the number of keys on the subtree rooted by x (including x's key)
    def sizeOf(self, x):
        if x == None:
            return 0
        return 1 + self.sizeOf(x.left) + self.sizeOf(x.right)

    def haT(self):
        return math.floor(math.log(self.size, 1.0 / self.a))

    # Determine if a specific depth of a node makes the tree "deep"
    def isDeep(self, depth):
        return depth > self.haT()

    # Returns the brother node of "node", whose parent is "parent"
    def brotherOf(self, node, parent):
        if parent.left != None and parent.left.key == node.key:
            return parent.right
        return parent.left

    # Builds a new binary tree based on an old one. The new tree is balanced
    def myRebuildTree(self, root, length):
        # Turn a binary tree into a list of nodes in sorted order
        def flatten(node, nodes):
            if node == None:
                return
            flatten(node.left, nodes)
            nodes.append(node)
            flatten(node.right, nodes)

        # Build a balanced binary tree for a sort list of nodes
        def buildTreeFromSortedList(nodes, start, end):
            if start > end:
                return None
            mid = int(math.ceil(start + (end - start) / 2.0))
            node = Node(nodes[mid].key)
            # node = nodes[mid]
            node.left = buildTreeFromSortedList(nodes, start, mid - 1)
            node.right = buildTreeFromSortedList(nodes, mid + 1, end)
            return node

        nodes = []
        flatten(root, nodes)
        return buildTreeFromSortedList(nodes, 0, length - 1)

    # Returns the node with the minimum key in the subtree rooted by x
    def minimum(self, x):
        while x.left != None:
            x = x.left
        return x

    # Delete the node in the tree with a value of delete_me
    def delete(self, delete_me):
        node = self.root
        parent = None
        is_left_child = True
        # find the node, keep track of the parent, and side of the tree
        while node.key != delete_me:
            parent = node
            if delete_me > node.key:
                node = node.right
                is_left_child = False
            else:
                node = node.left
                is_left_child = True

        successor = None
        # case 1: Node to be delete has no children
        if node.left == None and node.right == None:
            pass
        # case 2: Node has only a right child
        elif node.left == None:
            successor = node.right
        # case 3: Node has only a left child
        elif node.right == None:
            successor = node.left
        # case 4: Node has right and left child
        else:
            # find successor
            successor = self.minimum(node.right)
            # the successor is the node's right child -- easy fix
            if successor == node.right:
                successor.left = node.left
            # complicated case
            else:
                #print "finding successor"
                successor.left = node.left
                tmp = successor.right
                successor.right = node.right
                node.right.left = tmp

        # Replace the node
        if parent == None:
            self.root = successor
        elif is_left_child:
            parent.left = successor
        else:
            parent.right = successor

        self.size -= 1
        if self.size < self.a * self.max_size:
            # print "Rebuilding the whole tree"
            self.root = self.myRebuildTree(self.root, self.size)
            self.max_size = self.size

    def search(self, key):
        x = self.root
        while x != None:
            if x.key > key:
                x = x.left
            elif x.key < key:
                x = x.right
            else:
                return x;

        return None

    def insert(self, key):
        z = Node(key)
        y = None
        x = self.root
        # keep track of the depth and parents (so we don't have to recalculate
        # them)
        depth = 0
        parents = []
        # find where to place the node
        while x != None:
            parents.insert(0, x)
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
            depth += 1

        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        self.size += 1
        self.max_size = max(self.size, self.max_size)

        # Need to do rebuild?
        if self.isDeep(depth):
            scapegoat = None
            parents.insert(0, z)
            sizes = [0] * len(parents)
            I = 0
            # find the highest scapegoat on the tree
            for i in range(1, len(parents)):
                sizes[i] = sizes[i - 1] + self.sizeOf(self.brotherOf(parents[i - 1], parents[i])) + 1
                if not self.isAWeightBalanced(parents[i], sizes[i] + 1):
                    scapegoat = parents[i]
                    I = i
                    # print "When inserting %d Node %d is not weight balanced and could be a scapegoat" % (key, parents[I].key)

            tmp = self.myRebuildTree(scapegoat, sizes[I] + 1)

            scapegoat.left = tmp.left
            scapegoat.right = tmp.right
            scapegoat.key = tmp.key

    def isAWeightBalanced(self, x, size_of_x):
        a = self.sizeOf(x.left) <= (self.a * size_of_x)
        b = self.sizeOf(x.right) <= (self.a * size_of_x)
        return a and b

    def preOrder(self, x):
        if x != None:
            #print x.key, x.predecessor, x.distance
            self.preOrder(x.left)
            self.preOrder(x.right)

    def printTree(self):
        self.preOrder(self.root)


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.predecessor = {}
        self.position_in_buckets = -1
        self.distance_from_source = -1

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def get_predecessor(self):
        return self.predecessor

    def set_predecessor(self, predecessor):
        self.predecessor = predecessor

    def get_position_in_buckets(self):
        return self.position_in_buckets

    def set_position_in_buckets(self, position):
        self.position_in_buckets = position

    def set_distance_from_source(self, distance):
        self.distance_from_source = distance

    def get_distance_from_source(self):
        return self.distance_from_source


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def alpha(self, startvertex, maxweigth, numberofvertexes):

        # vertexdistances = []
        # vertexpredecessor = []
        #buckets = []
        t = ScapeGoatTree(0.5)

        for i in range(1, numberofvertexes):
            #print(i)
            g.get_vertex(i).set_distance_from_source(999999999999999999999999999999999999)
            g.get_vertex(i).set_predecessor(i)
            #print(g.get_vertex(i).get_predecessor(), g.get_vertex(i).get_distance_from_source())

        for i in g.get_vertices():
            #print('i corrente ---->', i)

            curr_vertex = g.get_vertex(i)
            currNode = t.search(curr_vertex.get_id())
            if(currNode == None):
                t.insert(curr_vertex.get_id())
                currNode = t.search(curr_vertex.get_id())

            if(curr_vertex.get_id() == 1):
                currNode.set_predecessor(1)
                currNode.set_distance(0)
                curr_vertex.set_distance_from_source(0)

            #print ('currNode ---->', currNode)

            for neigbhor in g.get_vertex(i).get_connections():
                #print('valor id do vizinho', neigbhor.get_id())

                nbNode = t.search(neigbhor.get_id())
                if (nbNode == None):
                    t.insert(neigbhor.get_id())
                    nbNode = t.search(neigbhor.get_id())

                #print ('nbNode ---->', nbNode)

                current_vertex_dist = g.get_vertex(i).get_distance_from_source()
                neigbhor_dist = neigbhor.get_distance_from_source()


                if (neigbhor_dist > (current_vertex_dist + curr_vertex.get_weight(neigbhor))):
                    #print(curr_vertex.get_weight(neigbhor))

                    #if (neigbhor_dist != 999999999999999999999999999999999999):
                        #print(buckets[neigbhor_dist])
                        #if (len(buckets[neigbhor_dist]) != 0):
                            #buckets[neigbhor_dist].remove(neigbhor.get_id())

                    neigbhor.set_predecessor(g.get_vertex(curr_vertex))
                    nbNode.set_predecessor(curr_vertex.get_id())
                    #print(nbNode.get_predecessor())
                    neigbhor.set_distance_from_source(
                        current_vertex_dist + curr_vertex.get_weight(neigbhor))

                    nbNode.set_distance(current_vertex_dist + curr_vertex.get_weight(neigbhor))

                    #print('nova distancia ', neigbhor.get_distance_from_source())


        #print('info da arvore dp de rodar')

        return t.printTree()


if __name__ == '__main__':

    timer = CPUtimer.CPUTimer()
    instance_path = "ALUE/"

    file_list = [f for f in os.listdir(instance_path)
                 if f.endswith('.stp')]
    for filename in sorted(file_list):
        #print filename
        path = os.path.join(instance_path, filename)

        with open(path) as f:
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

            g = Graph()

            for i in range(numVertices + 1):
                g.add_vertex(i)

            for i in range(2, len(graph)):
                verticePeso = []
                verticePeso.append(int(graph[i][2]))
                verticePeso.append(int(graph[i][3]))
                #print (int(graph[i][1]))
                #print (int(graph[i][2]))
                #print (int(graph[i][3]))

                # g.add_edge(int(graph[i][2]), int(graph[i][3]), verticePeso)
                g.add_edge(int(graph[i][1]), int(graph[i][2]), int(graph[i][3]))

            

            timer.reset()
            timer.start()
            #for i in range(0, 2):
            caminho = g.alpha(1, 13, numVertices)
            #    timer.lap()
            timer.stop()
            
            if not os.path.exists("Output/Question" + str("1e")):
                try:
                    os.makedirs("Output/Question" + str("1e"))
                except OSError as exc: # Guard against race condition
                    raise

            output = open((os.getcwd()+"/Output/Question"+str("1e"))+"/"+filename, "w")
    
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
