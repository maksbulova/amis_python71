str_1 = int(input())
col_1 = int(input())
str_2 = int(input())
col_2 = int(input())

"""
Цвет клетки зависит от того, одинакова ли чётность её координат,
этот параметр и сравнивается.
"""


if abs(str_1%2 - col_1%2) == abs(str_2%2 - col_2%2):
	answer = "Yes"
else:
	answer = "No"

print(answer)	