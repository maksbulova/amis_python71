input_list = [int(i) for i in input("Список чисел ").split()]


def reverse(list):
    if len(list) > 0:
        print(list[-1])
        reverse(list[:-1])
    else:
        print()


reverse(input_list)
input()
