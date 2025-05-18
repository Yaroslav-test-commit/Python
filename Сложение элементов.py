def sum_list(list_1, list_2):
    len_1, len_2 = len(list_1), len(list_2)
    min_len = min(len_1, len_2)
    new_list = []
    for a in range(min_len):
        new_list.append(list_1[a] + list_2[a])
    if len_1 > len_2:
        new_list.extend(list_1[min_len:])
    else:
        new_list.extend(list_2[min_len:])
    return new_list


result = sum_list([1, 2, 3, 4, 5], [6, 7, 8])
print(result)