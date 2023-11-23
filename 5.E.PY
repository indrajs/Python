string=input("enter the string:")
n=string.split(' ')
lst=[]
print("the list of words:",n)
for i in n:
    if i not in lst:
        lst.append(i)
print(lst)
for i in lst:
    count=0
    for j in n:
        if i==j:
            count+=1
            print(i,count)
