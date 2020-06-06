a=1
b=1
result=[1,1]
sum1=0
for i in range(1,51):
    sum=a+b
    if(sum<4000000):
        result.append(sum)
        a=b
        b=sum
for i in range(0,len(result)):
    if(result[i]%2==0):
        sum1=sum1+result[i]
print("sum of even fibonacci series less than four million is:",sum1)
        
    
    
