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

def mult(g, x, y):
 
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        n = max(len(str(x)),len(str(y)))
        nby2 = n / 2
        
        a = x / 10**(nby2)
        b = x % 10**(nby2)
        c = y / 10**(nby2)
        d = y % 10**(nby2)
        
        ac = mult(g, a,c)
        bd = mult(g, b,d)
        ad_plus_bc = mult(g, a+b,c+d) - ac - bd
        
        prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

        return prod
