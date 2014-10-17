'''
Created on Sep 22, 2014

@author: junaed
'''


def is_prime(n):
    if n <= 1:
        return False
    if n % 2 ==0:
        return False
    i = 3
    while (i * i)<=n:
        if n % i == 0:
            return False
    return True

def count_same_digits(n):
    pass
    

N = input()
K = input()
L = input()

smallest_number = 1
for i in xrange(1,N):
    smallest_number *= 10

largest_number = 9
for i in xrange(1,N):
    largest_number *= 10
    largest_number += 9
    
for i in xrange(smallest_number, largest_number+1):
    if is_prime(i):
        
    


if __name__ == '__main__':
    pass