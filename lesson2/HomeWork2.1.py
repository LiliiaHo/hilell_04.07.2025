number = int(input("Enter the four digit integer:"))
thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
units = number % 10
print(thousands)
print(hundreds)
print(tens)
print(units)