from __future__ import print_function

import CPUtimer

from data3 import instance_iterator, print_solution

def solve(instance_path):
    timer = CPUtimer.CPUTimer()
    for instance in instance_iterator(instance_path):
        timer.reset()
        timer.start()
        instance_name, g, p1, p2 = instance
        for i in range(0, 3): 
            result = mult(g, p1, p2)
            timer.lap()
        timer.stop()
        print_solution(result, instance_name, '3a', timer)

def mult(g, p1, p2):
    
    pot1 = 0
    pot2 = 0
    R = []
    for i in range(0, len(p1) + len(p2)-1):
        R.append(0)

    for i in p1:
        pot2 = 0
        for j in p2:
            R[pot1 + pot2] = i * j + R[pot1 + pot2]
            pot2 += 1
        pot1 += 1
    
    return R
