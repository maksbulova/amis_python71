while True:
    input_list = [int(i) for i in input\
    ("Введіть натуральні числа через пробіл: ").split()]
    if len(input_list) > 1:
        break


max_of_list = input_list[0]
pred_max_of_list = input_list[0]


def maximmum(list):

    global pred_max_of_list
    global max_of_list

    if len(list) < 1:
        return pred_max(input_list)
    elif list[0] > max_of_list:
        max_of_list = list[0]
    maximmum(list[1:])

    return pred_max_of_list


def pred_max(list):

    global max_of_list
    global pred_max_of_list

    if len(list) < 1:
        return 1
    elif (list[0] < max_of_list) & (list[0] > pred_max_of_list):
        pred_max_of_list = list[0]
    pred_max(list[1:])


print(maximmum(input_list))
input()