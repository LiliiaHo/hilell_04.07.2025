def common_elements(first_list: list, second_list: list) -> set[int]:
    first_list = set(first_list)
    second_list = set(second_list)
    com_nums_set = first_list.intersection(second_list)
    return com_nums_set

mult_of_3_list = [ num for num in range(100) if num % 3 == 0]
mult_of_5_list = [ num for num in range(100) if num % 5 == 0]


assert common_elements(mult_of_3_list, mult_of_5_list) == {0, 75, 45, 15, 90, 60, 30}