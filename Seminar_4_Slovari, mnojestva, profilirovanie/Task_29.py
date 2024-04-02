# На вход программе подаются натуральные числа, как только пользователь введет 0
# ввод прекращается. Вывести наибольший элемент получившейся последовательности.
# Есть два кода с ошибками, нужно определить где ошибок меньше. 

n = int(input())
max_number = n                   # max_number = 1000
while n != 0:
    n = int(input())
    if max_number < n:           # if max_number > n:
        max_number = n

print(max_number)

#2.--------------------------
n = int(input())
max_number = -1
while n > 0:                         # while n < 0:
    if max_number < n:
        max_number = n               # n = max_number
    n = int(input())                 # был в 18 строке

print(max_number)                    # print(n)

    