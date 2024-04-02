n=1254
res=0
while n > 0:
    m = n % 10
    res = res + m
    n = n // 10
print(res)