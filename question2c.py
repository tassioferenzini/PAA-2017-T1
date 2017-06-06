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
        print_solution(P, W, items, instance_name, '2c', timer)


def knapsack(k, P, W):
    items = [(i + 1, w, p / w) for i, (p, w) in enumerate(zip(P, W))]
    numItens = len(P)
    numItensCount = 0
    pivot = 0
    lenItems = len(items)
    itemsaux = iter(items)

    while (numItensCount < numItens):

        i, w, r = next(itemsaux)
        pivot = pivot + r
        numItensCount = numItensCount + 1

    pivot = pivot/numItens

    x = [0] * len(P)
    weight = 0
    s = 0
    e = len(items)
    items = iter(items)
    menoresPivot = []

    # percorre caras maiores que o pivot
    while (s < e):
        i, w, r = next(items)
        if r >= pivot:
            if weight + w <= k:
                x[i - 1] = 1
                weight = weight + w
            else:
                x[i - 1] = (k - weight) / w
                weight = k
        else:
            menoresPivot.append([i, w, r])
        s = s + 1

    # Se ainda nao preencheu a capacidade total da mochila
    if weight < k:
        menoresPivot = sorted(menoresPivot, key=lambda t: t[2], reverse=True)
        for indice in range(len(menoresPivot)):
            i = menoresPivot[indice][0]
            w = menoresPivot[indice][1]
            r = menoresPivot[indice][2]
            if weight + w <= k:
                x[i - 1] = 1
                weight = weight + w
            else:
                x[i - 1] = (k - weight) / w
                weight = k

    return [(i + 1, fract) for i, fract in enumerate(x) if fract > 0]
