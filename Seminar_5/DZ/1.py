# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.




# def f(a, b):
#     degree = a**b
#     return degree

#2 рекурсия

def f(a, b):
    if b == 0:
        return 1
    else:
        return a * f(a, b-1)
    
a = 3
b = 5   
print(f(3, 5))