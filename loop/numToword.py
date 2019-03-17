num=input('enter the number:')
sum=0;
count=0
count2=0
while num > 0:
    count+=1
    d=num % 10
    sum=sum*10+d
    num=num/10
while sum>0:
    count2+=1
    d=sum%10
    sum=sum/10
    if d==1:
        print"one",
    elif d==2:
        print"two",
    elif d==3:
        print"three",
    elif d==4:
        print"four",
    elif d==5:
        print"five",
    elif d==6:
        print"six",
    elif d==7:
        print"seven",
    elif d==8:
        print"eight",
    elif d==9:
        print"nine",
    elif d==0:
        print"zero",
if count is not count2:
    for i in range(1,count):
        print"zero",
