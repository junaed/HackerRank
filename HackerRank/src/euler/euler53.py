'''
Created on Sep 25, 2014

@author: junaed
'''

from math import factorial

if __name__ == '__main__':
    input = raw_input()
    inputs = input.split(" ")
    NN = int(inputs[0])
    K = int(inputs[1])
    count = 0
    for N in xrange(1,NN+1): 
        factorial_N = factorial(N)
        r = 0
        current_value = factorial_N / (factorial(r) * factorial(N - r))
        if current_value > K:
#             print current_value
            count += 2
        r += 1
        while r <= (N - r):
            current_value = (current_value * (N - r + 1)) / r
            if current_value > K:
#                 print current_value
                count += 1
                if r != (N - r):
                    count += 1
            r += 1 
    
    print count
    pass
