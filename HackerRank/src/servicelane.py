'''
Created on Sep 23, 2014

@author: junaed
'''

def service():

    N,T = raw_input().split()
    N = int(N)
    T = int(T)    
    
    width = [int(x) for x in raw_input().split()]
#     print width
    
    for i in xrange(0, T):
        start,end = raw_input().split()
        start = int(start)
        end = int(end)
        
        max_width = min(width[start:end+1])
        print max_width

if __name__ == '__main__':
    service()
