# Задача №35.
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)
# Input: 5
# Output: yes

def prime_num(num):
    
    for div in range(2,num):
        if num%div==0: 
            return False
    return True

        
num=int(input("Введите число: "))
print(prime_num(num))

#2--------------------------------------- оптимизация с 800 итераций до 30
def prime_num(num):
    if num != 2 and num % 2 == 0:
        return False
    for div in range(3,int(num ** 0.5) + 1, 2):
        if num % div == 0: 
            return False
    return True

        
num=int(input("Введите число: "))
print(prime_num(num))

#3 вариант


def prime_num(num):
    if num not in (2, 3, 5, 7) and num % 2 == 0 and num % 3 ==0 and num % 5 == 0 and num % 7 == 0:
        return False
    for div in range(3,int(num ** 0.5) + 1, 2):
        if num % div == 0: 
            return False
    return True

        
num=int(input("Введите число: "))
print(prime_num(num))