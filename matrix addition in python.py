a=[[1,2],[3,4]]
b=[[1,2],[3,4]]
result=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range (len(b)):
        result[i][j]=a[i][j]+b[i][j]
print(result)
