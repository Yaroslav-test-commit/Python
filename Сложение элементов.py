my_list = [1, 2, 3, 4]
my_list_new = [1, 2, 3, 4, 5, 6]
max_len = max(len(my_list), len(my_list_new))
my_list_modified = my_list + [0] * (max_len - len(my_list))
my_list_new_modified = my_list_new + [0] * (max_len - len(my_list_new))
list_new = []
for i in range(max_len):
    list_new.append(my_list_modified[i] + my_list_modified[i])

print(list_new)