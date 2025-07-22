# lst = [0, 1, 0, 12, 3]
# lst = [0]
# lst = [1, 0, 13, 0, 0, 0, 5]
lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
new_lst = []
for i in lst:
    if i == 0:
        new_lst.append(i)
while 0 in lst:
    lst.remove(0)
lst.extend(new_lst)
print(lst)




