try:
    n = int(input("Enter year to check: "))
except ValueError:
    print("Please enter a valid year.")
if n%2 == 0:
    print (f"{n} is a leap year.")
else:
    print (f"{n} is not a leap year.")