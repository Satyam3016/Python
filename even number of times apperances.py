L1=[2,4,6,8,2,8,4,4]
L2=[]
for i in L1:
    if L1.count(i)%2==0:
        if i not in L2:
            L2.append(i)
            print(L2)