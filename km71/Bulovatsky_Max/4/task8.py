s_str = int(input())
s_col = int(input())
f_str = int(input())
f_col = int(input())

if (abs(s_str - f_str) <= 1) & (abs(s_col - f_col) <= 1):
	answer = "Yes"
else:
	answer = "No"

print(answer)