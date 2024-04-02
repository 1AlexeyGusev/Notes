# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой 
# планетой ту, орбита которой имеет самую большую площадь. Напишите функцию find_
# farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по 
# которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете,
# что у вашей звезды таких планет нет, зато искусственные спутники были были 
# запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий 
# длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет 
# из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется 
# по формуле S = pi*a*b, где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два
# шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую  площадь. Гарантируется, что самая далекая планета ровно одна
# 2) - Дан список размеров(длина, ширина) эллипсов 
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# Напишите функцию find_farthest_orbit(list_of_orbits), которая находит площадь
# самого большого эллипса и возвращает кортеж с его размерами.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b – длины и ширина 
# осей эллипса
# -   Площадь кругов учитывать не нужно, т.е если у эллипса a == b, то это круг.
# При решении задачи используйте списочные выражения.
# Гарантируется, что самый большой эллипс всего один.

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# s = lambda cur_tuple: cur_tuple[0] * cur_tuple[1]
#
# max_s = s(orbits[0])
# find_tuple = orbits[0]
#
# for cur_orbit in orbits[1:]:
# if cur_orbit[0] != cur_orbit[1]:
# cur_s = s(cur_orbit)
# if cur_s > max_s:
# max_s = cur_s
# find_tuple = cur_orbit
#
# print(find_tuple)

def find_farthest_orbit(list_of_orbits):
    filter_orbits = list(filter(lambda cur_orbit: cur_orbit[0] != cur_orbit[1], list_of_orbits))
    tuple_s = list(map(lambda cur_orbit: cur_orbit[0] * cur_orbit[1], filter_orbits))
    max_s = max(tuple_s)
    i_max_s = tuple_s.index(max_s)
    return filter_orbits[i_max_s]

orbits = [(10, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(find_farthest_orbit(orbits))