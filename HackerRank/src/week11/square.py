'''
Created on Oct 6, 2014

@author: junaed
'''
import sys

def my_pow(y):
    result = 1
    a = 2
    while y:
        if y & 1:
            result = (result * a) % 1000000007
        a = (a * a) % 1000000007
        y >>= 1
    return result

if __name__ == '__main__':
    old_stdin = sys.stdin
#     sys.stdin = open("square.txt",'r')
    
    test_cases = input()
    for test in xrange(0,test_cases):
        n = input()
        n+=1
        result = (2 + my_pow(n))
        if test > 0:
            sys.stdout.write("\n")
        sys.stdout.write(str(result))
    
    sys.stdin = old_stdin