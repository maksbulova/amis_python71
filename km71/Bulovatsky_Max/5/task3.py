list = [int(i) for i in input("Введіть еленти через пробіл: ").split()]

i = 0
answer = []

while i < len(list):
	if list.count(list[i]) == 1:
		answer.append(list[i])
	i+=1

print(answer)