list=[]
for i in range(0,5):
    n=int(input("Enter the num:"))
    if(n>100):
        list.append("over")
    else:
        list.append(n)
print(list)

