line = [int(i) for i in input("Введіть зріст школярів через пробіл: ").split()]
pita = int(input("Введіть зрість Петра: "))


i=0
while True:
	if pita > line[i]:
		num = i + 1
		break
	i+=1
	
print("Петро, встань під номером ", num, "!", sep="")		