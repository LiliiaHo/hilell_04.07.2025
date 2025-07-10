abcde = int(input("Please enter the five digit integer:"))
e = abcde % 10
d = (abcde % 100) // 10
c = (abcde % 1000) // 100
b = (abcde % 10000) // 1000
a = abcde // 10000
print (str(e) + str(d) + str(c) + str(b) + str(a))


