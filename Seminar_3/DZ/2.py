# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

list_1 = [1, 2, 6, 4, 5]
k = 3
# closest = list_1[0]

# for i in range(len(list_1)):
#     elem = list_1[i] - k
#     if elem <0:
#         elem = -1 * elem
# closest = mi
# closest_elem = min([abs(i - k) for i in range(len(list_1))])
# print(closest_elem)

# closest_element = min(list_1, key=lambda x: abs(x - k))
# print(closest_element)
razn=abs(list_1[0]-k)
req_elem = list_1[0]
for i in range (1, len(list_1)):
    if abs(list_1[i]-k)<razn:
        razn = abs(list_1[i]-k)
        req_elem = list_1[i]
print(req_elem)