def sum_list(list_1, list_2):
    len_1, len_2 = len(list_1), len(list_2)
    min_length = min(len_1, len_2)
    new_list = []
    for a, b in zip(list_1, list_2):
        new_list.append(a + b)
    if len_1 > len_2:
        new_list.extend(list_1[min_length:])
    else:
        new_list.extend(list_2[min_length:])
    return new_list


result = sum_list([1, 2, 3, 4, 5], [6, 7, 8])
print(result)