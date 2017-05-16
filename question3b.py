from __future__ import print_function

import CPUtimer

from data3 import instance_iterator, print_solution

prod = []

def solve(instance_path):
    timer = CPUtimer.CPUTimer()
    for instance in instance_iterator(instance_path):
        instance_name, g, p1, p2 = instance
        timer.reset()
        timer.start()
        result = mult(g, p1, p2)
        timer.stop()
        print_solution(result, instance_name, '3b', timer)

def mult(g, x, y):
    g-=1
    if g == 1:
        print(1)
        #return x[0]*y[0]
    else:
        n = max(len(x),len(y))
        print(x)
        print(y)
        print(n)
        nby2 = n / 2
        
        a = x[g] / 10**(nby2)
        b = x[g] % 10**(nby2)
        c = y[g] / 10**(nby2)
        d = y[g] % 10**(nby2)
        
        
        ac = mult(g, a,c)
        bd = mult(g, b,d)
        ad_plus_bc = mult(g, a+b,c+d) - ac - bd
        
        prod.append(ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd)

    return prod
