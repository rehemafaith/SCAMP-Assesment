# consider that :
# F(n) =  F(n-1) + F(n-2)
# and F(0) = 0
# and F(1) = 1


def fib(n):
   
    """This is a recursive function"""

    if n == 0 or n==1:
        return n
    elif n<0:
        print("please input a valid number") 
    
    else:
        return fib(n-1)+fib(n-2) 


num = input("Enter your value: ") 
print("Fibonacci sequence:")
for i in range(num):
    print(fib(i))
