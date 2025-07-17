lst = [1,2,3,4,5,6]
# lst = []
# lst = [1]
# lst = [1,2,3]
point = (len(lst) + 1) // 2
part1 = (lst[:point])
part2 = (lst[point:])
new_list = [part1,part2]
print(new_list)