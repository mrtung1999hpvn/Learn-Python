#Giải phương trình bậc nhất 2 ẩn
# a1x+b1y = c1
# a2x+b2y = c2

#D | a1  b1 |
#  | a2  b2 |

#Dx| c1  b1 |
#  | c2  b2 |

#Dy| a1  c1 |
#  | a2  c2 |

a1,b1,c1 = int(input('Nhập a1 : ')),int(input('Nhập b1 : ')),int(input('Nhập c1 : '))
a2,b2,c2 = int(input('Nhập a2 : ')),int(input('Nhập b2 : ')),int(input('Nhập c2 : '))

D = a1*b2-b1*a2
Dx = c1*b2-b1*c2
Dy = a1*c2-c1*a2

if D==0:
    if Dx+Dy ==0:
        print("Phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else:
    print(f"He PT co nghiem (x,y) : ({Dx/D},{Dy/D})")
