str = input("enter the string:")
total=0
L=str.split()
for i in L:
    if L.count(i)==1:
        total+=1
print("the total number of unique word appearances of the string is",total)