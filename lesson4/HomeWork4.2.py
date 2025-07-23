# lst = [1, 3, 5]
# lst = [6]
lst = []
if not lst:
    print(0)
else:
    sum_of_elem = sum(lst[::2])
    print(sum_of_elem * lst[-1])