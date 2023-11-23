dict1={}
for i in range(0,5):
    key=int(input("Enter a key:"))
    value=input("Enter a value:")
    dict1[key]=value
print("Dictionary in ascending order:",dict(sorted(dict1.items())))
print("Dictionary in descending order:",dict(sorted(dict1.items(),reverse=True)))
