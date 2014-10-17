'''
Created on Sep 22, 2014

@author: junaed
'''

import Queue

q = Queue.Queue()
def calculate(N):
    nsum = 0
    a = ((N - 1) / 3)
    a = (3 * (a * (a + 1))) / 2
    b = (N - 1) / 5
    b = (5 * (b * (b + 1))) / 2
    c = (N - 1) / 15
    c = (15 * (c * (c + 1))) / 2
    nsum = a + b - c
    return nsum

T = input()

for i in xrange(0, T):
    N = input()
    print calculate(N)
    
