# Задача №21. Напишите программу для печати всех уникальных значений в словаре.

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#         {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# Примечание: Список словарей задан изначально. Пользователь его не вводит

list_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

# uniq_val = set()

# for curr_dict in list_dicts:
#     for key in curr_dict:
#         uniq_val.add(curr_dict[key])
        
# print(uniq_val)

#------------------------------------------------------------------------

# uniq_val = set()

# for curr_dict in list_dicts:
#         uniq_val.add(*curr_dict.values())
        
# print(uniq_val)
#-----------------------------------------------------------------------------

uniq_val = set()

for curr_dict in list_dicts:
        uniq_val.update(curr_dict.values())
        
print(uniq_val)