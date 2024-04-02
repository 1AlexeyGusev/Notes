# Пользователь вводит одно число N. Далее идут N чисел, записанных на новой строчке
# каждое. вывести минимальное и максимальное.
# Input: 5 -> 5 1 6 5 9
# Output: 1 9
# from random import randint

# n = int(input("Введите число "))
# min_num = 1000
# max_num = 0

# for i in range(n):
#     num = randint(1, 10)
#     print(num, end = " ")
#     if max_num < num:
#         max_num = num
#     if min_num > num:
#         min_num = num
# print()        
# print(min_num, max_num)

#2.---------------------------------------------------------

from random import randint

n = int(input("Введите число "))
num = randint(1, 10)
min_num = num
max_num = num

for i in range(n-1):
    num = randint(1, 10)
    print(num, end = " ")
    max_num = max(max_num, num)
    min_num = min(min_num, num)
print()        
print(min_num, max_num)