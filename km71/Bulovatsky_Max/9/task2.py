a = int(input("Число "))
n = int(input("В степень "))


def power(x, y):
    a = x
    for i in range(y-1):
        a *= x
    return a

print(power(a, n))
