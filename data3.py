from __future__ import print_function

import os
import sys
import CPUtimer

def parse_instance(instance_file):
    
    with open(instance_file) as f:
        text = f.readlines()
        lines = [t.strip().split() for t in text]
        polynomialA = []
        polynomialB = []
        degree = int(lines[0][0])
        for line in lines[1:]:
            if polynomialA == []:
                polynomialA.append(line)
            else: 
                if line != []:
                    polynomialB.append(line)
    return degree, polynomialA, polynomialB

def instance_iterator(instance_path):
    file_list = [f for f in os.listdir(instance_path)
    if f.startswith('multp_2') and f.endswith('.dat')]
    for filename in sorted(file_list):
        path = os.path.join(instance_path, filename)
        g, p1, p2 = parse_instance(path)
        yield (filename[6:-4], g, p1, p2)

def print_solution(resultado, instance_name, question, timer):

    if not os.path.exists("Output/Question" + str(question)):
        try:
            os.makedirs("Output/Question" + str(question))
        except OSError as exc: # Guard against race condition
                raise

    output = open((os.getcwd()+"/Output/Question"+str(question))+"/"+"multp_"+instance_name+".dat", "w")
    
    output.write('{}\n'.format('Polinomio Resultante'))
    output.write('{}\n'.format(resultado))
    
    output.write("\n")
    output.write("Total time: " + str( timer.get_time() ) +" s")
    output.write("\nAverage time: " + str( timer.get_time("average","micro")) + " \u00B5s")
    output.write("\nLast call: " + str( timer.get_time("last","micro") ) +" \u00B5s")
    output.write("\nStamp 1 of the total: " + str( timer.get_stamp("total","si") ) ) 
    output.write("\nStamp 2 of the total: " + str( timer.get_stamp("total","clock") ) )
    output.write("\nPattern that ignores zeros:")
    output.write("\n" + timer.get_stamp("total","si",True))
    output.write("\n" + timer.get_stamp("total","clock",True))
