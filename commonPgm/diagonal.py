n=input("enter the order:")
mat=[]
for i in range(n):
    r=[]
    for j in range(n):
        x=input()
        r.append(x)
    mat.append(r)
for i in range(n):
    print mat[i],""
for i in range(n):
    for j in range(i+1,n):
        if i==j:
            continue
        elif(mat[i][j]<mat[j][i]):
            mat[j][i]=1
        else:
            mat[i][j]=0

print"matrix after operation"
for i in range(n):
    print mat[i],""

