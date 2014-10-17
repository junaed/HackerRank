'''
Created on Sep 22, 2014

@author: junaed
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

def calculate_value(n):
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n%2 == 0:
        return (2 * (calculate_value(n-2))) + 2
    else:
        return (2 * (calculate_value(n-2))) + 1

rows = input()
for row in xrange(0,rows):
    n = input()
    print calculate_value(int(n)+1)