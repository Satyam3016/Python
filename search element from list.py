L=[2,58,95,999,65,32,15,1,7,45]
n=int(input("Enter the number to be searched : "))
if n in L: 
	print("Item found at the Position : ",L.index(n)+1)
else:
    print("Item not found in list")