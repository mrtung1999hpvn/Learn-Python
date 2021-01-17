def SoHH(n):
    Tong = 0
    for i in range(1,n,1):
        if n%i ==0:
            Tong = Tong +i
        if Tong == n:
            return True
    return False

def GCD(a,b):
    if (b==0):
        return a
    return GCD(b,a%b)

def BCNN(a,b):
    return a*b / GCD(a,b)
    

print(SoHH(28))

print(10%3)
