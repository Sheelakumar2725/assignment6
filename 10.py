x=int(input("enter a num1:"))
y=int(input("enter a num2:"))
z=int(input("enter a num3:"))
if x>y and x>z:
    print("the greatest number is:",x)
elif y>x and y>z:
    print("the greatest number is:",y)
else:
    print("the greatest number is:",z)
