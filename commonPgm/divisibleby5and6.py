num=input("enter anumber:")
temp=False
if num%5==0 and num%6==0:
    temp=True
else:
    temp=False
print"Is divisible by 5 and 6?",temp
if num%5==0 or num%6==0:
    temp=True
else:
    temp=False
print"Is divisible by 5 or 6?",temp
if num%5==0 or num%6==0:
    if num%5==0 and num%6==0:
        temp=False
    else:
        temp=True
else:
    temp=False
print"Is divisible by 5 or 6,but not both?",temp