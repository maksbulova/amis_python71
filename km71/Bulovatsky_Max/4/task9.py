s_str = int(input())
s_col = int(input())
f_str = int(input())
f_col = int(input())

if (abs(s_str - f_str) == abs(s_col - f_col)):
	answer = "Yes"
else:
	answer = "No"

print(answer)