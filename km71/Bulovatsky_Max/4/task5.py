a = int(input())
b = int(input())
c = int(input())

if a == b == c :
	answer = 3
elif (a == b) | (a == c) | (b == c):
	answer = 2
else:
	answer = 0

print(answer)	