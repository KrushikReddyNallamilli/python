num=int(input("Enter numerator:"))
den=int(input("Enter denominator:"))
try:
    quo=num/den
except ZeroDivisionError:
    print("we can't divide with zero")
else:
    print(quo)
