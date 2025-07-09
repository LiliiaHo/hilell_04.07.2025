abcde = input("Please enter the five digit number: ")
a = int(abcde) // 10000
b = (int(abcde) % 10000) // 1000
c = (int(abcde) % 1000) // 100
d = (int(abcde) % 100) // 10
e = int(abcde) % 10
print(e)
print(d)
print(c)
print(b)
print(a)