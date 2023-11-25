def fibonaci(n):
    a=0
    b=1
    fib=0
    if n==0:
        return a
    elif n==1:
        return b
    else:
        print(a)
        print(b)
    for i in range(2,n):
        fib=a+b
        a=b
        b=fib
        print(fib)
n=int(input("Enter a number:"))
fibonaci(n)
