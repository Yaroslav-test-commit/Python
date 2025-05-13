def sum_list(list_1, list_2):
    list_new = []
    if len(list_1) != len(list_2):
        if len(list_1) > len(list_2):
            diff = len(list_1) - len(list_2)
            for i, v in enumerate(list_1):
                if i >= len(list_1) - diff:
                    list_new.append(v)
                else:
                    list_new.append(v + list_2[i])
        else:
            diff = len(list_2) - len(list_1)
            for i, v in enumerate(list_2):
                if i >= len(list_2) - diff:
                    list_new.append(v)
                else:
                    list_new.append(v + list_1[i])
    else:
        for i, v in enumerate(list_1):
            list_new.append(v + list_2[i])
    return list_new


result = sum_list([1, 2, 3, 5, 7], [4, 5, 6, 7])
print(result)
