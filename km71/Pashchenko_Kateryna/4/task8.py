#Визначити, чи може король перейти з першої клітини у другу за один хід
x1 = int(input('Введіть номер стовпчика першої клітинки:'))
y1 = int(input('Введіть номер рядка пешої клiтинки:'))
x2 = int(input('Введіть номер стовпчика другої клітинки:'))
y2 = int(input('Введіть номер рядка другої клiтинки:'))
if ((1<= x1<=8) or (1<=y1<=8)or (1<=x2<=8)or(1<=y2<=8)):
    if ((x1==x2)and (y1==y2)):
        answer = 'NO'
    else:
        if((x2==x1+1 or x2 == x1-1) and (y1==y2)): # фігура пeреходить на одну клітинку вправо або вліво, залишаючсь в цьому ж самому рядку
            answer = 'YES'
        elif((y2 == y1+1  or y2 == y1+1) and (x1==x2)): #Фігура переходить на одну клітинку вверх або вниз, залишаючись в цьому ж самому стовпчику
            answer = 'YES'
        elif(((x2 == x1+1) and(y2==y1-1)) or((x2 == x1-1) and (y2 == y1-1))):# фігура переміщається по діагоналі
            answer = 'YES'
        elif(((x2 == x1+1) and (y2 == y1+1)) or ((x2 == x1 -1)and(y2 == y1 +1))):#фігура переміщаеться по діагоналі на судідню клітинку
            answer = 'YES'
        else:
            answer = 'NO'
else:
    answer = 'Ви ввели некоректне число'
print(answer)
