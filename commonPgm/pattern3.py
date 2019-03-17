n=input("enter the limit:")
p=0
for i in range(1,n+1):
    print
    p+=2
    for j in range(n-i):
        print" ",

    for k in range(1,i+1):
        print "*",

    for m in range(i-1,0,-1):
        print "*",