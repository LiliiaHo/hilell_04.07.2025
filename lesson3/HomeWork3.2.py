lst = [12, 3, 4, 10]
# lst = [1]
# lst = []
# lst = [12, 3, 4, 10, 8]
if len(lst) <= 1:
    print(lst)
elif len(lst) > 1:
    moved_element = lst.pop(-1)
    lst.insert(0, moved_element)
    print(lst)