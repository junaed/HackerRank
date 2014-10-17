'''
Created on Sep 23, 2014

@author: junaed
'''

def calculate_fib(N):
    fibs = []
    first = 1
    second = 2
    
    while second <= N:
        if second %2 == 0:
            fibs.append(second)
        first, second = second, first+second
    return fibs
    
    
if __name__ == '__main__':
    N = 40000000000000000
    fibs = calculate_fib(N)
#     print "done"
    T = input()
    
    for i in xrange(0,int(T)):
        n = input()
        x = 0
        sum = 0
        while x< len(fibs) and fibs[x] <= n:
            sum += fibs[x]
            x+=1
            
        print sum