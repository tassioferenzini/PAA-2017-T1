# -*- coding: cp1252 -*-
from __future__ import print_function

import sys
import os

import question1
import question2a
import question2b
import question3
import CPUtimer

QUESTIONS = {
    '1': question1.solve,
    '2a': question2a.solve,
    '2b': question2b.solve,
    '3': question3.solve,
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
	print("Average time: " + str( timer.get_time("average","micro") ) +" \u00B5s")
	print("Last call: " + str( timer.get_time("last","micro") ) +" \u00B5s")
	print("Stamp 1 of the total: " + str( timer.get_stamp("total","si") ) ) 
	print("Stamp 2 of the total: " + str( timer.get_stamp("total","clock") ) )
	print("\nPattern that ignores zeros:")
	print( timer.get_stamp("total","si",True) )
	print( timer.get_stamp("total","clock",True) )

if __name__ == '__main__':
    main()
