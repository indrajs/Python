list=[]
r=int(input("Enter the range:"))
for i in range(0,r):
    n=int(input("Enter the element:"))
    list.append(n)
print("The list isv:",list)
list=[i*i for i in list]
print("list of sqaures",list)
