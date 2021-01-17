from math import *

def GT(n):
    gt=1
    for i in range(1,n+1,1):
        gt*=i
    return gt
    
s=1.0
n=1
ep = float(input('ep : '))
x = float(input('x : '))

while (abs(x**n) / GT(n) >= ep ):
    s += abs(x**n) / GT(n)
    n+= 1
    
print(s)
print(str(exp(x)))
