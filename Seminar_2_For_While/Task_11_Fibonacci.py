# n = int(input("Введите число: "))
# count = 4
# fib1 = 1
# fib2 = 1
# fib3 = fib1 + fib2

# while fib3 < n:
#     fib1 = fib2
#     fib2 = fib3
#     fib3 = fib1 + fib2
#     count += 1
    
# if fib3 ==n:
#     print(count)
# else:
#     print(-1)
    
    
    
###################################################################

n = int(input("Введите число: "))
count = 4
fib1 = 1
fib2 = 2

while fib2 < n:
    fib1, fib2 = fib2, fib1+fib2
    count += 1
    
if fib2 ==n:
    print(count)
else:
    print(-1)