a=int(input("enter month number:"))
if a in(1,3,5,7,8,10,12):
    print("31 days")
elif a in(4,6,9,11):
    print("30 days")
elif a==2:
    print("29 or 28 days")
else:
    print("invalid month number")
