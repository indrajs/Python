list=[]
total=0
for i in range(0,3):
    n=int(input("Enter a number:"))
    list.append(n)
print(list)
for i in list:
    total=total+i;
print("Sum of all items in list:",total)
