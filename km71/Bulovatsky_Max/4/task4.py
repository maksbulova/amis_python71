year = int(input())

if (((year%4) == 0) & ((year%100) != 0)) | ((year%400) == 0):
	answer =  "LEAP"
else:
	answer = "СOMMON"

print(answer)