n=int(input())
m=int(input())
k=int(input())

if (k<n*m) & ((k%n==0) | (k%m==0)):
    answer = "Yes"
else:
	answer = "No"

print(answer)