sum=0
for i in range(1,201):
    c=0
    for j in range (1,i+1):
        if (i%j==0):
            c=c+1
    if(c==2):
        sum=sum+i
print("sum of prime numbers from 1 to 200 is",sum)
        
