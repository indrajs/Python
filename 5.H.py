string1=input("Enter the first string:")
string2=input("Enter the second string:")
string3=string2[0]+string1[1:]+""+string1[0]+string2[1:]
print("New string:",string3)
