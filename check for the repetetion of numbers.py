def dups():
    list=[]
    n=int(input("Enter length of list: "))
    while(n!=0):
        num=int(input("Enter number : "))
        list.append(num)
        n=n-1
    print(set(x for x in list if list.count(x)>1))
dups()
