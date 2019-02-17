num=input("enter a num:")
temp=num
a=0
while(num>0):
    d=(num%10)
    d=d*d*d
    a=a+d
    num=int(num/10)
print(a)
if(a==temp):
    print("amstrong")
    
