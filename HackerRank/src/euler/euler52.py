'''
Created on Sep 24, 2014

@author: junaed
'''

def get_digits(n):
    return sorted(str(n))

def same_digits(n, multiplier):
    digits = get_digits(n)
    res = [n]
    for i in xrange(1, multiplier):
        m = get_digits(n + (i * n))
        if digits != m or str(m).startswith('0'):
#             res.append(n + (i * n))
#             return False
            break
        else:
            res.append(n + (i * n))
    return res

if __name__ == '__main__':
    input = raw_input()
    inputs = input.split(" ")
    N = int(inputs[0])
    K = int (inputs[1])
#     K = 6
    line = 0
    if K == 2:
        start = 125874
        end = min(N,1492857)
    elif K == 3 or K == 4 or K == 5 or K==6:
        start = 142857
        end = min(N,1429857)
    else:
        start = 125874
        end = N
    for i in xrange(start, end + 1):
        r = same_digits(i, K)
        if len(r) == K:
            if line > 0:
                    print ""
            for x in r:                
                print x,
                line += 1
