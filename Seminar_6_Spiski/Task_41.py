# 1) Дан массив, состоящий из целых чисел. Напишите программу, которая в данном 
# массиве выведет количество элементов, у которых два соседних и, при этом, оба 
# соседних элемента меньше данного. Сначала вводится число N — количество элементов
# в массиве  Далее записаны N чисел — элементы массива. Массив состоит из целых
# чисел. 
# 2) (пользовательский ввод можно заменить на рандомный)
# Пользователь вводит  размер массива – N
# и элементы массива (целые числа). 
# нужно из этого массива вывести количество элементов, у которых ближайшие соседние
# элементы меньше самого элемента.
# Ввод: 			Ввод:
# 5			5
# 1 2 3 4 5			1 5 1 5 1

# Вывод:			Вывод:
# 0			2

from random import randint


size_list = randint(5,10)
# for _ in range(size_list):
#     list_1.append(randint(1,5))
    
list_1 = [randint(1,5) for _ in range (size_list)]

# list_1 = []

print(list_1)

count = 0

for i in range(1, size_list-1):
    if list_1[i-1]<list_1[i] > list_1[i+1]:
        count += 1
print(count)

