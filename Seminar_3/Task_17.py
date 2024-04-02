# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1,1,2,0,-1,3,4,4]
# Output: 6
from random import randint


size = int(input("Введите размер списка: "))
# list_1 = []
# for _ in range(size):
#     list_1.append(randint(-5,5))
   
list_2 = [randint(-5,5) for _ in range(size)]  ## создаем список с помощью list comprehension (то же самое, что мы сделали в 8-10 строках)

print(list_2)
# unique_nums = set(list_2)
# print(len(unique_nums)) 
print(len(set(list_2))) # то же самое, что и в 15-16 строках