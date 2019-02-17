num1 = int(input("enter the first num:"))
num2 = int(input("enter the 2nd num:"))
num3 = int(input("enter the 3rd num:"))
if num1 > num2:
    if num1 > num3:
        print(num1)
elif num2 < num3:
    print(num3)
else:
    print(num2)
