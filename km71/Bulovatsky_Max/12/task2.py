def Max(list):
    global a
    if len(list) == 1:
        a = list[0]
    else:
       a = max(int(Max(list[:-1])), int(list[-1]))
    return a


def count(list):
    Max(list)
    return list.count(str(a))


print(count(input("please write a list ").split()))
input()