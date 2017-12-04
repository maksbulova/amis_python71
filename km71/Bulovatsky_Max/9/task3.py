x = int(input("Число "))
y = int(input("В степень "))

def power(a, n):
    if n > 0:
        result = a * power(a, n-1)
    else:
        return 1    
    return result

print(power(x, y))
input()