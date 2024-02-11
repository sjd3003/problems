try:
    n = int(input("What is your number: "))
except ValueError:
    print ("Please Enter an Integer.")

if n%2 == 0:
    print (f"{n} is an even number.")
else:
    print (f"{n} is an odd number.")