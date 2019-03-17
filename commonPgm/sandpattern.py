n=input("enter the limit:")
p=0
count=n;


for i in range(n-1):
    print
    for j in range(i):
        print" ",

    for k in range(1,n+1-i):
        print k+i," ",
for i in range(1,n+1):
    print
    p+=2
    for j in range(n-i):
        print" ",

    for k in range(i):
        print count+k," ",
    count-=1


