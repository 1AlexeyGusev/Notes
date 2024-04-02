# n = int(input("Введите число N: "))
# count = 1
# fact = 1
# while count <= n:
#     fact *= count
#     count += 1
# print(fact)

########################################################

n = int(input("Введите число N: "))
fact = 1
while n > 1:
    fact *= n
    n -= 1
print(fact)
    