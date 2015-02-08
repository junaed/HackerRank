'''
Created on Nov 18, 2014

@author: junaed
'''

if __name__ == '__main__':
    m = input()
    ar = [int(i) for i in raw_input().strip().split()]
    ar = sorted(ar)
    min_count=1
    current_low=ar[0]
    current_high=current_low+4
    for i in xrange(1,m):
        if ar[i]>= current_low and ar[i]<=current_high:
            continue
        else:
            min_count+=1
            current_low=ar[i]
            current_high=current_low+4
    print min_count
        
    pass