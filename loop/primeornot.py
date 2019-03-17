num=input('enter a number')
if num==2:
    print "number is prime"
else:
    for i in range(2,num):
        if num%i==0:
            break
    if num==i+1:
        print "number is prime"
    else:
        print "number is not prime"
