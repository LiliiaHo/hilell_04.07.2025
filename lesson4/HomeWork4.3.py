import random
full_list = [random.randint(1, 100) for i in range(random.randint(3, 10))]
print(full_list)
tree_elem = [full_list[0], full_list[2], full_list[-2]]
print(tree_elem)

