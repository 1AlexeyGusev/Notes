# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , разность d и количество элементов n будет задано автоматически. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
a1 = 2
d = 3
n = 4

list_1 = []
for n in range(1, n+1):
    list_1.append(a1 + (n-1)*d)
for i in range(len(list_1)):
    print(list_1[i])