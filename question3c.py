from __future__ import print_function

import CPUtimer
import cmath
from scipy.fftpack import fft, ifft

from data3 import instance_iterator, print_solution

def solve(instance_path):
    timer = CPUtimer.CPUTimer()
    for instance in instance_iterator(instance_path):
        instance_name, g, p1, p2 = instance
        timer.reset()
        timer.start()
        for i in range(0, 2): 
            result = ifft(fft(p1)*fft(p2))
            timer.lap()
        timer.stop()
        print_solution(result, instance_name, '3c', timer)
