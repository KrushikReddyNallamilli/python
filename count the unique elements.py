def unique():
    list=[]
    n=int(input("Enter the length of the list : "))
    while(n!=0):
        num=int(input("Enter the number: "))
        list.append(num)
        n=n-1
    print(set(x for x in list if list.count(x)==1))
unique()
