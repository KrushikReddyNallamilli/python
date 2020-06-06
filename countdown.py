import time
n=int(input("enter number to start countdown="))
while n>=0:
    print(n)
    time.sleep(1)
    n=n-1
print("blast")
