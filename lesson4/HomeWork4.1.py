lst = [0, 1, 0, 12, 3]
# lst = [0]
# lst = [1, 0, 13, 0, 0, 0, 5]
# lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
lst_without_0 = []
lst_0 = []
for i in lst:
    if i > 0:
        lst_without_0.append(i)
    elif i == 0:
        lst_0.append(i)
new_list = lst_without_0 + lst_0
print(new_list)




