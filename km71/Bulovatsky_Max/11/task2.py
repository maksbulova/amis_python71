input_list = [int(i) for i in input("Список чисел ").split()]

min_of_list = input_list[0]


def minimum(list):
    global min_of_list
    if len(list) < 1:
        return 1
    elif list[0] < min_of_list:
        min_of_list = list[0]
    minimum(list[1:])
    return min_of_list


print(minimum(input_list))
input()
