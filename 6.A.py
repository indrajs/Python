n=int(input("Enter the number:"))
if(n<=0):
    print("The factorial is:0")
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i;
print("The factorial is:",fact)
    
