list = [int(i) for i in input("Введіть еленти через пробіл: ").split()]

i = 0
k = 1
answer = 0

# проверим не повторится ли элемент "правее" от места текущего элемента

while i < len(list):
	while i + k < len(list):			
		if list[i] == list[i+k]:
			answer+=1
		k+=1	
	k=1
	i+=1

print("Пар у списку:", answer)