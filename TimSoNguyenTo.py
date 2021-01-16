import random

n = int(input('Nhập n: '))

_list = [random.randint(1,100) for i in range(n)]

print(_list)

def SoNT(a):
    if a < 2 :
        return False
    for i in range(2,a,1):
        if(a%i==0):
            return False
    return True
    
for i in _list:
    print(f'{i} La so nguyen to' if (SoNT(i)) else f'{i} Khong la so nguyen to')
