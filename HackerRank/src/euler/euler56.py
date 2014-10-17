'''
Created on Oct 14, 2014

@author: junaed
'''

def my_pow(a, y):
    result = 1
#     a = 2
    while y:
        if y & 1:
            result = (result * a)
        a = (a * a)
        y >>= 1
    return result

def get_digit_sum(n):
    sum1 = 0
    while n>0:
        sum1 += (n%10)
        n = n / 10
    return sum1

if __name__ == '__main__':
    N = input()
    max_sum = 0
    for i in xrange(1,N):
        for j in xrange(1,N):
            current = my_pow(i,j)
            c_max = get_digit_sum(current)
            if c_max > max_sum:
                max_sum = c_max
    print max_sum
    