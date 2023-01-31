# ДЗ. Задача 3. 
# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

bilet = int(input("Введите шестизначный номер билета: "))
num1 = bilet // 1000
num2 = bilet % 1000

numDigit1 = 0
summ1 = 0
numDigit2 = 0
summ2 = 0
while num1 != 0 and num2 != 0:  # работает также и при условии OR
    numDigit1 = num1 - num1 % 10
    summ1 = summ1 + (num1 - numDigit1)
    num1 = num1 // 10
    numDigit2 = num2 - num2 % 10
    summ2 = summ2 + (num2 - numDigit2)
    num2 = num2 // 10

if summ1 == summ2:
    print("yes")
else:
    print("no")