current=int(input("Enter the current year:"))
final=int(input("enter the final year"))
print("the leap years are:")
for i in range(current,final):
    if(i%400==0 or(i%100!=0 and i%4==0)):
        print(i)
