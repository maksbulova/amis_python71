point_1 = [int(i) for i in input('Введите через пробел \
две координаты 1ой точки: ').split()]
point_2 = [int(i) for i in input('Введите через пробел \
две координаты 2ой точки: ').split()]


def distance(point1, point2):
    return (((point2[0] - point1[0])**2) + (point2[1] - point1[1])**2)**0.5

print(distance(point_1, point_2))
