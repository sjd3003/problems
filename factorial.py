def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter number: "))
x= factorial(n)
print (f"{n}! = {x}")
print(f"Factorial of {n} is {x}.")
