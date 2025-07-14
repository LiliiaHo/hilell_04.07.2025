number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
action = input("Enter the operation: ")
if action == "plus" or action == "+":
    print (number1 + number2)
elif action == "minus" or action == "-":
    print (number1 - number2)
elif action == "divide" or action == "/":
    if number2 != 0:
        print(number1 / number2)
    else:
        print ("Impossible operation")
elif action == "multiply" or action == "*":
    print (number1 * number2)
else: print("Unknown operation")