'''
Created on Sep 23, 2014

@author: junaed
'''

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

if __name__ == '__main__':
    T = input()
    for i in xrange(0,T):
        n = input()
        print max(prime_factors(n))