from __future__ import print_function

import CPUtimer

from data3 import instance_iterator, print_solution

def solve(instance_path):
    timer = CPUtimer.CPUTimer()
    for instance in instance_iterator(instance_path):
        instance_name, g, p1, p2 = instance
        timer.reset()
        timer.start()
        result = mult(g, p1, p2)
        timer.stop()
        print_solution(result, instance_name, '3a', timer)

def mult(g, p1, p2):
    
    producto = []
        
    for i in range(0, g):
        for j in range(0, g):
            producto.append(int(p1[i])*int(p2[j]))
            
    return producto
