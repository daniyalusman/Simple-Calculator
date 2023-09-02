num_1 = int(input("Enter 1st Number: "))
operator = input("Enter Operator +, -, *, /: ")
num_2 = int(input("Enter 2nd Number: "))

if operator == "+":
    print(num_1 + num_2)
elif operator == "-":
    print(num_1 - num_2)
elif operator == "*":
    print(num_1 * num_2)
elif operator == "/":
    print(num_1 / num_2)
else:
    print("Please enter valid operator")
