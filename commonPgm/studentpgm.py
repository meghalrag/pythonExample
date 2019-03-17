slimit=input("how many students:")
stud=[]
mark=[]
sum=0
avg=0
highest=0
for i in range(slimit):
    print"enter name of student",i+1,":",
    x=raw_input()
    stud.append(x)
for i in range(slimit):
    print"enter mark of stud:",i+1,":",
    x=input()
    mark.append(x)
    if(mark[i]>highest):
        highest=mark[i]
print "si.no     ","name          ","mark"
for i in range(slimit):
    print i+1,".      ",stud[i],"             ",mark[i]
for i in range(slimit):
    sum=sum+mark[i]
avg=sum/slimit
print""
print"*****average of mark******",avg
print"students below average list:"
print""
print "si.no     ","name          ","mark"
for i in range(slimit):
    if(mark[i]<avg):
        print i + 1, ".      ", stud[i], "             ", mark[i]
print""
print"students list with highest mark:"
print""
print "si.no     ","name          ","mark"
for i in range(slimit):
    if(mark[i]==highest):
        print i + 1, ".      ", stud[i], "             ", mark[i]


