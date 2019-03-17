nfile=open('negative.txt','a+',1)
pfile=open('positive.txt','a+',1)
l=nfile.readlines()
m=pfile.readlines()
# l=['good','bad']
# sfile=open('sss','r',1)
yourstr=raw_input("enter your string:")
list=yourstr.split()
nc=pc=0
for i in range(len(list)):
    list[i]+='\n'
for i in list:
    if i in l:
        nc+=1
    elif i in m:
        pc+=1
if 'not' in yourstr:
    if pc>nc:
        print 'your feeling sad'
    elif nc!=0:
        print 'your feeling happy'
    else:
        print"no idea"
else:
    if nc>pc:
        print "your feeling sad"
    if nc==pc:
        print"no idea"
    elif pc!=0:
        print"your feeling happy"
    else:
        print'no idea'