dict1={}
dict2={}
for i in range(0,2):
    key1=int(input("Enter a key of dict1:"))
    value1=input("Enter value of dict1:")
    dict1[key1]=value1
for i in range(0,2):
    key2=int(input("Enter a key of dict2:"))
    value2=input("Enter value of dict2:")
    dict2[key2]=value2
dict1.update (dict2)
print(dict1)
