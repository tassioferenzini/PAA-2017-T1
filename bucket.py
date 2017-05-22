import os
import sys
import CPUtimer

from sys import argv, exit

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

    def buckets(self, startvertex, maxweigth, numberofvertexes):

        buckets = []

        for i in range(1, numberofvertexes):
            #print(i)
            g.get_vertex(i).set_distance_from_source(999999999999999999999999999999999999)
            g.get_vertex(i).set_predecessor(i)
            #print(g.get_vertex(i).get_predecessor(), g.get_vertex(i).get_distance_from_source())

        for i in range(0, (numberofvertexes * maxweigth + 1)):
            buckets.append([])

        #print(buckets, len(buckets))

        buckets_index = 0
        buckets[0].append(startvertex+1)
        #print(buckets[0])
        #print(len(buckets[0]))
        g.get_vertex(buckets[0][0]).set_distance_from_source(0)
        #print(g.get_vertex(buckets[0][0]).get_distance_from_source())

        while (1):

            while (len(buckets[buckets_index]) == 0 and buckets_index < numberofvertexes * maxweigth):
                buckets_index = buckets_index + 1
            if buckets_index == numberofvertexes * maxweigth:
                break
            #print('buckets index----------->', buckets_index)
            #print('buckets[%d] antes do pop ')
            #print(buckets)
            current_vertex = buckets[buckets_index].pop()
            #print('vertice corrent')
            #print(current_vertex)
            #print('buckets dp do pop ')
            #print(buckets[buckets_index])
            hasNb = g.get_vertex(current_vertex).get_connections()
            #print 'hasNb=>', len(hasNb)

            #if hasNb == 0 and buckets_index < numberofvertexes * maxweigth:
                #print 'vertice sem conexcoes'

            for neigbhor in g.get_vertex(current_vertex).get_connections():
                #print('valor do vizinho', neigbhor.get_id())

                current_vertex_dist = g.get_vertex(current_vertex).get_distance_from_source()
                neigbhor_dist = neigbhor.get_distance_from_source()

                #print('current_vertex_dist')
                #print(current_vertex_dist)
                #print('neigbhor dist')
                #print(neigbhor_dist)
                #print(g.get_vertex(current_vertex))
                x = g.get_vertex(current_vertex)
                wn = x.get_weight(neigbhor)

                #print("peso visinho", wn)

                if (neigbhor_dist > (current_vertex_dist + g.get_vertex(current_vertex).get_weight(neigbhor))):
                    #print(g.get_vertex(current_vertex).get_weight(neigbhor))

                    if (neigbhor_dist != 999999999999999999999999999999999999):
                        #print(buckets[neigbhor_dist])
                        if (len(buckets[neigbhor_dist]) != 0):
                            buckets[neigbhor_dist].remove(neigbhor.get_id())

                    neigbhor.set_predecessor(g.get_vertex(current_vertex))
                    #print(neigbhor.get_predecessor())
                    neigbhor.set_distance_from_source(
                        current_vertex_dist + g.get_vertex(current_vertex).get_weight(neigbhor))
                    #print('nova distancia ', neigbhor.get_distance_from_source())
                    neigbhor_dist = neigbhor.get_distance_from_source()
                    buckets[neigbhor_dist].insert(0, neigbhor.get_id())
                    #print(buckets[neigbhor_dist])

        #print('info do grafo dp de rodar')

        #for vertex in g.get_vertices():
            #print('vertex ->', g.get_vertex(vertex).get_id())
            #print('distancia da origem', g.get_vertex(vertex).get_distance_from_source())
            #print 'predecessor ', g.get_vertex(vertex).get_predecessor()

        caminho = []

        i=numberofvertexes-1
        caminho.append(i)
        i = g.get_vertex(i)
        while(1):

            pred = i.get_predecessor()
            #print g.get_vertex(pred)

            if pred == 0:
                caminho.append(pred)
                break
            if pred == i.get_id():
                #print('parou')
                break

            caminho.append(pred.get_id())
            i = pred
        return caminho

if __name__ == '__main__':
    
    instance_path = "DMXA/"
    timer = CPUtimer.CPUTimer()
    
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
         
            for i in range(numVertices+1):
                g.add_vertex(i)

            for i in range(2, len(graph)):
                verticePeso = []
                verticePeso.append(int(graph[i][2]))
                verticePeso.append(int(graph[i][3]))
                #print (int(graph[i][1]))
                #print (int(graph[i][2]))
                #print (int(graph[i][3]))

                #g.add_edge(int(graph[i][2]), int(graph[i][3]), verticePeso)
                g.add_edge(int(graph[i][1]), int(graph[i][2]), int(graph[i][3]))

            timer.reset()
            timer.start()
            for i in range(0, 2):
                caminho = g.buckets(1, 13, numVertices)
                sorted(caminho, reverse=True)
                timer.lap()
            timer.stop()
            
            if not os.path.exists("Output/Question" + str("1d")):
                try:
                    os.makedirs("Output/Question" + str("1d"))
                except OSError as exc: # Guard against race condition
                    raise

            output = open((os.getcwd()+"/Output/Question"+str("1d"))+"/"+filename, "w")
    
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
