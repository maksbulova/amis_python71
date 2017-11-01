minuts = int(input("Введіть хвилини "))
minuts_result = minuts % 60
hours = minuts // 60
hours_result = hours % 24
print(hours_result, minuts_result, sep=":")
