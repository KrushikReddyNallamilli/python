x1=int(input("Enter x1: "))
x2=int(input("Enter x2: "))
y1=int(input("Enter y1: "))
y2=int(input("Enter y2: "))
r1=int(input("Enter radius 1: "))
r2=int(input("Enter radius 2: "))
distance=(((x2-x1)**2+(y2-y1)**2)**0.5)
radius=r1+r2
if(distance<=radius):
    print("balls collide")
else:
       print("balls does not collide")
