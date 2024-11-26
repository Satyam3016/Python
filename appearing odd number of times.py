l1=[1,5,87,90,789,789,5,5,5]
l2=[]
for i in l1:
    if l1.count(i)%2!=0:
        if i not in l2:
         l2.append(i)
        print(l2)
