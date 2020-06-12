import math
def gcd(num1,num2):
    return math.gcd(num1,num2)
def lcm(num1,num2):
    return((num1*num2)//gcd(num1,num2))
num1=int(input("enter num1"))
num2=int(input("enter num2"))
ngcd=gcd(num1,num2)
nlcm=lcm(num1,num2)
print("lcm:",nlcm)
print("GCd:",ngcd)
