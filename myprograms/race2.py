import thread
import time
import random
lis=[]
def fun(name,ti):
    i = 0
    while i<n:
        i+=1
        lis.append(name)
        print name,
        time.sleep(ti)
    print'\n'
    winner.append(name)
no=input("no:of raisers:")
print'raisers name:'
na=[]
winner=[]
for i in range(no):
    print i+1,
    temp=raw_input()
    na.append(temp)
n=input("enter raise length:")
for i in range(no):
    thread.start_new_thread(fun,(na[i],random.randint(1,5)))
while 1:
    if len(winner)==no:
        j=0
        for i in winner:
            j+=1
            if j==1:
                print '1st is ',i
            elif j==2:
                print '2nd is ',i
            elif j==3:
                print '3rd is ',i
            else:
                if j==4:
                    print 'loosers:'
                print i
        break