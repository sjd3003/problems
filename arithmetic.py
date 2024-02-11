#getting input from user
num_1 = int(input("What is your first number? "))
num_2 = int(input("What is your second number? "))

sum = num_1 + num_2
deduct = num_1 - num_2
multi = num_1 * num_2
if num_1 > num_2:
    div = num_1 / num_2
else:
    div = num_2 / num_1

print(f"Addition of these two number is {sum}.")
print (f"{num_1} + {num_2} = {sum}")
print(f"Deduction of these two number is {deduct}.")
print (f"{num_1} - {num_2} = {deduct}")
print(f"Multiplication of these two number is {multi}.")
print (f"{num_1} * {num_2} = {multi}")
print(f"Division of these two number is {div}.")
if num_1 > num_2:
    print (f"{num_1} / {num_2} = {div}.")
else:
    print (f"{num_2} / {num_1} = {div}.")

