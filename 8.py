a=int(input("enter a n1:"))
b=int(input("enter a n2:"))
c=int(input("enter a n3:"))
d=b**2-4*a*c
if d>0:
    print("real and distinct roots")
elif d==0:
    print("real and equal roots")
else:
    print("imaginary roots")
