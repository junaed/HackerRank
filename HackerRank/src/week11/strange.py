'''
Created on Oct 7, 2014

@author: junaed
'''
import sys
import Queue

def another_strange():
    start = [5, 6, 7, 8, 9]
    q = Queue.Queue()
    for i in start:
        q.put(i)
    strange = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    LIMIT = 1000000000000000000
    min_number = [0, 0]
    max_number = [0, 9]
    l = 1
    h = 9
    for i in xrange(2, 19):
        l *= 10
        min_number.append(l)
        h *= 10
        h += 9
        max_number.append(h)
    while not q.empty():
        item = q.get()
        strange.add(item)
#         print item
        for i in xrange(2, 19):
            if item >= (min_number[i] / i) and item <= (max_number[i] / i):
                x = item * i
                if x <= LIMIT and x % 2 == 0:
                    q.put(x)
    return sorted(strange)
    
if __name__ == '__main__':
    old_stdin = sys.stdin
#     sys.stdin = open("strange.txt", 'r')
    list_str = another_strange()
#     
    test_cases = input()
    for test in xrange(0, test_cases):
        line = raw_input()
        line = line.split(" ")
        L = int(line[0])
        R = int(line[1])
#         print L, R
        count = 0
        li = 0
        sz = len(list_str)
        while li < sz and list_str[li] < L:
            li += 1
        hi = sz - 1
        while hi >=0 and list_str[hi] > R:
            hi -= 1
        count = hi - li + 1
        
        if test > 0:
            sys.stdout.write("\n")
        sys.stdout.write(str(count))
#     
    sys.stdin = old_stdin
