# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
import os
import pip

import question1a
import question1b
import question1c
import question1d
import question1e
import question2a
import question2b
import question2c
import question3a
import question3b
import question3c
import CPUtimer

QUESTIONS = {
    '1a': question1a.solve,
    '1b': question1b.solve,
    '1c': question1c.solve,
    '1d': question1d.solve,
    '1e': question1e.solve,
    '2a': question2a.solve,
    '2b': question2b.solve,
    '2c': question2c.solve,
    '3a': question3a.solve,
    '3b': question3b.solve,
    '3c': question3c.solve,
}

def usage():
    print('trabalho <instance_path> [ {} ]'.format(' | '.join(QUESTIONS.keys())))

def main():
    # Instanciano a CPU timer  
    timer = CPUtimer.CPUTimer()
    print("")
    print("Measuring Code Time:\n")
    timer.reset()
    timer.start()
    if len(sys.argv) != 3:
        print('Error: missing arguments!\n') 
        usage() 
        return
        
    if not os.path.exists(sys.argv[1]): 
        print('Error: <instance_path> not found!\n')
        usage()
        return
        
    if sys.argv[2] not in QUESTIONS:
        print('Error: unknown question {}!\n'.format(sys.argv[2]))
        usage()
        return
        
    _, instance_path, question = sys.argv
    QUESTIONS[question](instance_path)
    
    timer.stop()
    print('\nQuestion: {}\n'.format(sys.argv[2]))
    print("Total time: " + str( timer.get_time() ) +" s")
    print("Average time: " + str( timer.get_time("average","seg") ) +" s")
    print("Last call: " + str( timer.get_time("last")) +" s")
    print("Stamp 1 of the total: " + str( timer.get_stamp("total","si") ) ) 
    print("Stamp 2 of the total: " + str( timer.get_stamp("total","clock") ) )
    print("\nPattern that ignores zeros:")
    print( timer.get_stamp("total","si",True) )
    print( timer.get_stamp("total","clock",True) )

if __name__ == '__main__':
    pip.main(['install', "scipy"])
    main()
