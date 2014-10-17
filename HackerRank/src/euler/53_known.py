from math import factorial

def ncr(n,r):
    return (factorial(n)/(factorial(r)*factorial(n-r)))

i = 0
uniq = set()
for x in range(1,101):
    for y in range(0,x):
        if(ncr(x,y) > 1000000):
#             print ncr(x,y)
#             uniq.add(ncr(x,y))
            i=i+1

print i
# print len(uniq)