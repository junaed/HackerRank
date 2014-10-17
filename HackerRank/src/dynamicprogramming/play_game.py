'''
Created on Oct 2, 2014

@author: junaed
'''

import sys

if __name__ == '__main__':
    old_stdin = sys.stdin
#     sys.stdin = open("play_game.txt","r")
    
    test_cases = input()
    
    for test in xrange(test_cases):
        t_elements = input()
        elements = raw_input()
        elements = elements.split(" ")
        a = [int(x) for x in elements]
        a = a[::-1]
        a.insert(0,0)
        p_sum = [0]
        s = 0
        for x in a[1:]:
            s += x
            p_sum.append(s)
        dp = [0]
        dp.append(a[1])         #1 
        dp.append(dp[1]+a[2])   #2
        dp.append(dp[2]+a[3])   #3
        
        for i in xrange(4, t_elements+1):
            m = max(p_sum[i-1] - dp[i-1] + a[i], p_sum[i-2] - dp[i-2] + a[i] + a[i-1], p_sum[i-3] - dp[i-3] + a[i] + a[i-1] + a[i-2])
            dp.append(m)
#         print a
#         print p_sum
#         print dp
        print dp[t_elements]
    
    sys.stdin = old_stdin