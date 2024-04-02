# Пользователь вводит число N (1 <= N <=10).
# Далее построчно N чисел от -50 до 50. Нужно вывести наиболшее 
# количество идущих пожряд положительных чисел.
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2
# import random

# num = int(input("Введите количество дней: "))
# count = 0
# max_count = 0
# for i in range(num):
#     t = random.randint(-50, 50)
#     print(t, end = " ")
#     if t > 0:
#         count += 1
#         if max_count < count:
#             max_count = count
#     else:
#         count = 0
# print()
# print(max_count)

### 2.----------------------------------------------------------------

import random

num = int(input("Введите количество дней: "))
count = 0
max_count = 0
for i in range(num):
    t = random.randint(-50, 50)
    print(t, end = " ")
    if t > 0:
        count += 1
        
    else:
        if max_count < count:
            max_count = count
        count = 0
if max_count < count:
    max_count = count
print()
print(max_count)
