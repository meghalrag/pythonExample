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
    if no*n== len(lis):
        print winner
        print '1st=',winner[0]
        print '2nd=',winner[1]
        print '3rd=',winner[2]
# ra=random.randint(1,5)
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
time.sleep(no*n*5)