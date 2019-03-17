string=raw_input("enter the plaintext:")
length=len(string)
string2=" "
if length==1 or length==2:
    print "cipher text:",string
else:
    list=[]
    print "string length:",length
    for i in range(1,length,1):
        sqr=i*i
        if sqr==length or sqr>length:
            n=i;
            break
    print "square matrix",n,"x",n
    count=0
    flag=0
    for i in range(n):
        r=[]
        for j in range(n):
            r.append('.')
        list.append(r)

    for i in range(n):
        for j in range(n):
            list[i][j]=string[count]
            if string[count]==' ':
                list[i][j]='*'
            count += 1
            if count == length :
                flag=1
                break
        if flag==1:
            break
    for i in range(n):
        print list[i]," "
    print"\n ****Cipher text****"
    for i in range(n):
        for j in range(n):
            print list[j][i],
    for i in range(n):
        for j in range(n):
            string2+=list[j][i]
    # print string2
    print "\nplain text:"
    list2=[]
    count=1
    for i in range(n):
        r=[]
        for j in range(n):
            r.append(string2[count])
            count+=1
        list2.append(r)
    # print list2
    for i in range(n):
        for j in range(n):
            if list2[j][i]=='*':
                list2[j][i]=" "
            if list2[j][i]=='.':
                continue
            print list2[j][i],
