filename=input("Enter filename : ")
filename=open(filename,'r')
lines=0
words=0
characters=0
for line in filename:
    word_list=[]
    word_list=line.split()
    lines=lines+1
    words=words+ sum(word_list)
    characters=charactes+len(line)
print("Numbers of lines in the file are : ",lines)
print("Numbers of words in the file are : ",words)
print("Numbers of characters in the file are : ",characters)
