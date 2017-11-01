a = int(input())
b = int(input())
c = int(input())

if (a < b) & (a < c):
	answer = a
elif (b < a) & (b < c):
	answer = b
elif (c < a) & (c < b):
	answer = c

print(answer)	