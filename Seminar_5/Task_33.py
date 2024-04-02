# Задача №33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая 
# заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1

from random import randint
import time

n=int(input("Введите количество оценок: "))
list_1=[randint(1,5) for _ in range(n)]
print(list_1)
start_1 = time.time()
max_point=max(list_1)
min_point=min(list_1)
for i in range(len(list_1)):
    if list_1[i]==max_point:
        list_1[i]=min_point
end_1 = time.time()
print(list_1)

#2.------------------------------------------------------------------

start_2 = time.time()
max_point=list_1[0]
min_point=list_1[0]
for i in range(1, len(list_1)):
    if list_1[i]>max_point:
        max_point = list_1[i]
    if list_1[i]<min_point:
        min_point = list_1[i]
        
for i in range(len(list_1)):
    if list_1[i]==max_point:
        list_1[i]=min_point     
end_2 = time.time()  
print(list_1)
print(f'{end_1 - start_1}')
print(f'{end_2 - start_2}')
