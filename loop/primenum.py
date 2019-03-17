n=input("enter the limit:")

n=n+2
j=2
while j<n:
   # print "iter=",j
    #print"limit=", n
    for k in range(2,j+1):
        #print "k=", k
        if j%k==0:
            break
    if(k==j):
        print j,
    else:
        n=n+1
        #print"n=",n
    j+=1
