num = input("enter a number:")
sum=0
temp=num
while num > 0:
    d=num % 10
    sum=sum*10+d
    num=num/10
if sum==temp:
    print("palindrome")
else:
    print("not palindrome")


