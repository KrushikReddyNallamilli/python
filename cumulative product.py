def c_p():
    list=[1,2,3,4,5,6,7,8,9,10]
    product=1
    for i in range(0,len(list)):
        product=product*list[i]
    print("cum prod=",product)
c_p()
