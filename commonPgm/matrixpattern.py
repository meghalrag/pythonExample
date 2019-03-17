n=input("enter the limit:")
mat=[]
d=[]
c=0
m=0
for i in range(n):
    r=[]
    for j in range(n):
        r.append('')
    mat.append(r)
for i in range(n):
    for j in range(i,n-i,1):
        c+=1
        mat[i][j]=c
        if j==n-1-i:
            for k in range(i+1,n-i,1):
                c+=1
                mat[k][j]=c
                if k==n-i-1:
                    for l in range(n-i-2,i-1,-1):
                        c+=1
                        mat[k][l]=c
                        if l==i:
                            for m in range(n-i-2,i,-1):
                                c+=1
                                mat[m][l]=c

# for i in range(n):
#     print""
#     for j in range(n):
#         print mat[i][j],
for i in range(n):
    print mat[i],""



