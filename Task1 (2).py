def factorial(num):
    f=1
    for i in range(1, num+1):
        f*= i
    return f

var=int(input("Enter a number: "))
print(f"Factorial of {var} is: {(factorial(var))}")



