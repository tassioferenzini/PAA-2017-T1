from __future__ import print_function

import os
import sys
import CPUtimer

def parse_instance(instance_file):
    
    with open(instance_file) as f:
         text = f.readlines()
         lines = [t.strip().split() for t in text]
         nb_items = int(lines[0][0])
         P = [0] * nb_items
         W = [0] * nb_items
         
         for line in lines[1:]:
             if line[1:2]:
                 index = int(line[0])
                 profit = int(line[1])
                 weight = int(line[2])
                 P[index - 1] = profit
                 W[index - 1] = weight
             else:
                knapsack_size = int(line[0])
         return knapsack_size, P, W

def instance_iterator(instance_path):
    file_list = [f for f in os.listdir(instance_path)
    if f.startswith('m') and f.endswith('.in')]
    for filename in sorted(file_list):
        path = os.path.join(instance_path, filename)
        k, P, W = parse_instance(path)
        yield (filename[1:-3], k, P, W)

def _print_solution(nb_items_used, total_weight, total_profit, items_fractions, instance_name, question, timer):

    if not os.path.exists("Output/Question" + str(question)):
        try:
            os.makedirs("Output/Question" + str(question))
        except OSError as exc: # Guard against race condition
                raise

    output = open((os.getcwd()+"/Output/Question"+str(question))+"/"+"m"+instance_name+".in", "w")
    
    output.write('{} \t{} \t{} \n'.format('Number of items','Total Weight',    'Total Profit'))
    output.write('{} \t{} \t{} \n'.format(nb_items_used, total_weight, total_profit))
    
    output.write("\n\n")
    output.write("Total time: " + str( timer.get_time()) +" s")
    output.write("\nAverage time: " + str( timer.get_time("average", "seg")) + " s")
    output.write("\nLast call: " + str( timer.get_time("last")) +" s")
    output.write("\nStamp 1 of the total: " + str( timer.get_stamp("total","si"))) 
    output.write("\nStamp 2 of the total: " + str( timer.get_stamp("total","clock")))
    output.write("\nPattern that ignores zeros:")
    output.write("\n" + timer.get_stamp("total","si",True))
    output.write("\n" + timer.get_stamp("total","clock",True))
    output.write("\n\n")
    output.write("Item    Fraction\n\n")
    items = sorted(items_fractions, key=lambda t: t[0])
    for item, fract in items:
        output.write('{} \t{}\n'.format(item, fract))

def print_solution(P, W, items_fractions, instance_name, question, timer):
    
    nb_items_used = len(items_fractions)
    total_weight = sum(W[item - 1] * fract for item, fract in items_fractions)
    total_profit = sum(P[item - 1] * fract for item, fract in items_fractions)
    _print_solution(nb_items_used, total_weight, total_profit, items_fractions, instance_name, question, timer)
