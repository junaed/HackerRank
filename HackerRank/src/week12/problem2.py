'''
Created on Nov 18, 2014

@author: junaed
'''
import math

if __name__ == '__main__':
    m = input()
    ar = [int(i) for i in raw_input().strip().split()]
    x_coef=2
    subt=ar[0]
    for i in xrange(1,m):
        x_coef*=2
        subt*=2
        subt+=ar[i]
#     print subt
#     print x_coef
    print int(math.ceil(float(subt)/float(x_coef)))
    pass