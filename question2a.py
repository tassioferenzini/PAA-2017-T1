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
		print_solution(P, W, items, instance_name, '2a', timer)

def knapsack(k, P, W):
    items = [(i + 1, w, p / w) for i, (p, w) in enumerate(zip(P, W))]
    #print (items, "\n")
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
			#print (e)
			break
    return [ (i + 1, fract) for i, fract in enumerate(x) if fract > 0]
