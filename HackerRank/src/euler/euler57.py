'''
Created on Oct 14, 2014

@author: junaed
'''
import fractions

def get_num_digits(n):
    return len(str(n))
        

if __name__ == '__main__':
    N = input()
    
    n = 3
    d = 2
    c = 0
    for i in xrange(1,N):
        n += 2*d
        d = n - d
        if get_num_digits(n) > get_num_digits(d):
            print i+1
            c+=1
    print c 