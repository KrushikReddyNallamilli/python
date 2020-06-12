def rev():
    list=[]
    rlist=[]
    n=int(input("Enter the lengeth of the list :"))
    while(n!=0):
        num=int(input("Enter elemnts in the list:"))
        list.append(num)
        n=n-1
    for i in range(len(list)-1,-1,-1):
        rlist.append(list[i])
    print(rlist)
rev()
