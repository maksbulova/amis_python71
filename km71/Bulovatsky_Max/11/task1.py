result = ""


def input_type(type):
    global result
    if type == "natural":
        print("Input ", type)
        result = input()
        if not result.isdigit():
            input_type(type)
        result = int(result)
    elif type == "string":
        print("Input ", type)
        result = input()
    return result


i = 0
y = 0


def task(x, n):
    global i
    global y
    i += 1
    if i > n:
        return y
    y += (x-i)/(i**2)
    return task(x, n)

x = input_type("natural")
n = input_type("natural")

print(task(x, n))
input()
