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
        for i in range(0, 2):
            items = knapsack(k, P, W)
            timer.lap()
        timer.stop()
        print_solution(P, W, items, instance_name, '2a', timer)

def knapsack(k, P, W):
    items = [(i + 1, w, p / w) for i, (p, w) in enumerate(zip(P, W))]
    items = iter(sorted(items, key=lambda t: t[2], reverse=True))
    x = [0] * len(P)
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
            break
    return [ (i + 1, fract) for i, fract in enumerate(x) if fract > 0]
