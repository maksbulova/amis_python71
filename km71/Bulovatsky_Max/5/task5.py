qn_1 = [int(i) for i in input('Введите через пробел две координаты 1ого ферзя: ').split()]
qn_2 = [int(i) for i in input('Введите через пробел две координаты 2ого ферзя: ').split()]
qn_3 = [int(i) for i in input('Введите через пробел две координаты 3его ферзя: ').split()]
qn_4 = [int(i) for i in input('Введите через пробел две координаты 4ого ферзя: ').split()]
qn_5 = [int(i) for i in input('Введите через пробел две координаты 5ого ферзя: ').split()]
qn_6 = [int(i) for i in input('Введите через пробел две координаты 6ого ферзя: ').split()]
qn_7 = [int(i) for i in input('Введите через пробел две координаты 7ого ферзя: ').split()]
qn_8 = [int(i) for i in input('Введите через пробел две координаты 8ого ферзя: ').split()]
qn_all = [qn_1, qn_2, qn_3, qn_4, qn_5, qn_6, qn_7, qn_8]

i=0
k=1
str=0
col=1
answer = "никто ниого не бьёт"

while (i+1 < len(qn_all)):
	while (i+k+1 < len(qn_all)):
		if (abs(qn_all[i][str] - qn_all[i+k][str])) == (abs(qn_all[i][col] - qn_all[i+k][col])) | ((qn_all[i][str] == qn_all[i+k][str]) | (qn_all[i][col] == qn_all[i+k][col])):
			answer = "кто-то кого-то бьёт"
			i = len(qn_all)
		k+=1
	i+=1
	k=1		


print(answer)