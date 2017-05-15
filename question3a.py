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
        
    for i in range(0, g+1):
        for j in range(0, g+1):
            producto.append(int(p1[0][i])*int(p2[0][j]))
            
    return producto
