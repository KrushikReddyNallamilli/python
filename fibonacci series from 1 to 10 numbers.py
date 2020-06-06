a=1
b=2
sum=0
result=[1,2]
for i in range(1,11):
    sum=a+b
    result.append(sum)
    a=b
    b=sum
print("fibonacci series from 1 to 10 numbers is :",result)
