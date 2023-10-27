name=[]
c=0
for i in range(0,4):
    e=input("enter the names")
    name.append(e)
for i in name:
    c+=i.count('a')
print("count of 'a' in the list is ",c)
