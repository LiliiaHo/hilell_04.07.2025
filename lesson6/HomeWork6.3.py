entered = input("Enter the integer: ")
while (len(entered)) > 1:
    res = 1
    for digit in entered:
        res *= int(digit)
    entered = str(res)
print(entered)