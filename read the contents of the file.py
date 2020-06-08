filename=input("Enter filename")
file=open(filename)
list=file.readlines()
file.close()
dict={}
for line in list:
    for char in line:
        if char not in dict:
            dict[char]=1
        else:
            dict[char]+=1
print(dict)
