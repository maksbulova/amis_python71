N, K = [int(i) for i in input("Введите через пробел количество кеглей и бросков: ").split()]
line = [1 for i in range(N)]

for i in range(K):
    l, r = [int(i) for i in input("Введи через пробел пару чисел li и ri: ").split()]
    for i in range(l-1, r):
        if line[i] == 1:
            line[i] = 0

for i in line:
    if i == 1:
        print('|', end='')
    else:
        print('.', end='')