list=[]
r=int(input("Enter the range:"))
for i in range(0,r):
    n=int(input("Enter the element:"))
    list.append(n)
    list=[i for i in list if i>0]
print("The list is:",list)
print(list)
