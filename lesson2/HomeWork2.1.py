number = input("Enter the four digit integer:")
thousands = int(number) // 1000
hundreds = (int(number) % 1000) // 100
tens = (int(number) % 100) // 10
units = int(number) % 10
print(thousands)
print(hundreds)
print(tens)
print(units)