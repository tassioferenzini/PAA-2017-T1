from __future__ import print_function
from __future__ import division

import CPUtimer

from data2 import instance_iterator, print_solution

def solve(instance_path):
    timer = CPUtimer.CPUTimer()
    for instance in instance_iterator(instance_path):
        instance_name, k, P, W = instance
        timer.reset()
        timer.start()
        items = knapsack(k, P, W)
        timer.stop()
        print_solution(P, W, items, instance_name, '2b', timer)

def knapsack(k, P, W):
    items = [(i + 1, w, p / w) for i, (p, w) in enumerate(zip(P, W))]
    #pivot = findMoM(items)
    pivot = selectPivot(items, k)
    x = [0] * len(P)
    weight = 0
    s = 0
    e = len(items)
    items = iter(items)
   
    while (s < e):
        i, w, r = next(items)
        if r >= pivot[2]:
            x[i - 1] = 1
            weight += w
        s +=1

    if weight < k:
        x[i - 1] = (k - weight) / pivot[1]
        weight = k
        
    return [ (i + 1, fract) for i, fract in enumerate(x) if fract > 0]

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

def selectPivot(A, capacity):

    k = findMoM(A)
    Left =[]
    Right = []
    totalRight = 0
    s = 0
    e = len(A)

    while(s < e):
        if(A[s][0] != k[0]):
            if A[s][2] < k[2]:
                Left.append(A[s]) 
            else:
                totalRight += A[s][1]
                Right.append(A[s])
        s += 1    

    if totalRight == capacity:
        return k 
    else: 
        if totalRight < capacity:
            if totalRight + k[1] >= capacity:
                return k            
            else:
               return selectPivot(Left, capacity-totalRight-k[1])
        else:
            return selectPivot(Right, capacity)