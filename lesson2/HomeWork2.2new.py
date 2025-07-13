abcde = int(input("Please enter the five digit integer:"))
e = abcde % 10 * 10000
d = (abcde % 100) // 10 * 1000
c = (abcde % 1000) // 100 * 100
b = (abcde % 10000) // 1000 * 10
a = abcde // 10000
print(e + d + c + b + a)
