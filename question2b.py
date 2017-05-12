from __future__ import print_function
from __future__ import division

import CPUtimer

from data2 import instance_iterator, print_solution

def solve(instance_path):
    timer = CPUtimer.CPUTimer()
    #print('Question 2 a\n')
    for instance in instance_iterator(instance_path):
        instance_name, k, P, W = instance
        #print('Solving', instance_name)
        timer.reset()
        timer.start()
        items = knapsack(k, P, W)
        timer.stop()
        #print_solution(P, W, items, instance_name, '2a', timer)

def knapsack(k, P, W):
    items = [(i + 1, w, p / w) for i, (p, w) in enumerate(zip(P, W))]
    print ("MoM", findMoM(items))
    #items = iter(sorted(items, key=lambda t: t[2], reverse=True))
    '''x = [0] * len(P)
    weight = 0
    while weight < k:
        try:
            i, w, _ = next(items)
            if weight + w <= k:
                x[i - 1] = 1
                weight += w
            else:
                x[i - 1] = (k - weight) / w
                weight = k
        except Exception as e:
            #print (e)
            break
    return [ (i + 1, fract) for i, fract in enumerate(x) if fract > 0]'''

def findMoM(A):

    #Divide A in (n/5) groups of 5 and sort them.
    #Find the median of the ratio (value/weight) of each (n/5) group and the possible group 
    #with mod 5 elements and store them in M.
    #Find recursively the median of the set M and store the index of the median in k

    if(len(A) == 1):
        return A[0]
        
    M = []
    numGroups = len(A) // 5   
    i = 0

    while(i < numGroups):
        j = (5*i)
        Temp = sorted(A[j:j+5], key=lambda t: t[2], reverse=True)        
        M.append(Temp[2])
        i += 1

    if(len(A) % 5 > 0):
        Temp = sorted(A[(5*i):], key=lambda t: t[2], reverse=True)
        M.append(Temp[((len(Temp) + 1) // 2)-1])

    return findMoM(M)
