lst = [12, 3, 4, 10]
if len(lst) <= 1:
    print(lst)
elif len(lst) > 1:
    moved_element = lst.pop(-1)
    lst.insert(0, moved_element)
    print(lst)

lst = [1]
if len(lst) <= 1:
    print(lst)
elif len(lst) > 1:
    moved_element = lst.pop(-1)
    lst.insert(0, moved_element)
    print(lst)

lst = []
if len(lst) <= 1:
    print(lst)
elif len(lst) > 1:
    moved_element = lst.pop(-1)
    lst.insert(0, moved_element)
    print(len(lst))

lst = [12, 3, 4, 10, 8]
if len(lst) <= 1:
    print(lst)
elif len(lst) > 1:
    moved_element = lst.pop(-1)
    lst.insert(0, moved_element)
    print(lst)

lst = [0]
if len(lst) <= 1:
    print(lst)
elif len(lst) > 1:
    moved_element = lst.pop(-1)
    lst.insert(0, moved_element)
    print(lst)

lst = [4]
if len(lst) <= 1:
    print(lst)
elif len(lst) > 1:
    moved_element = lst.pop(-1)
    lst.insert(0, moved_element)
    print(lst)