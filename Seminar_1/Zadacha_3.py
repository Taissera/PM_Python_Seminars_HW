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

# Разбор ДЗ на семинаре:
# ticket_number = int(input())

# sum_first = 0
# sum_last = 0

# while ticket_number:
#     digit = ticket_number % 10        # берем последнюю цифру числа
#     if ticket_number > 999:           # проверка, что tikcket_number не трёхзначное число. 
#         sum_first += digit
#     else:
#         sum_last += digit             # эта строка начинает работать, когда условие tikcket_number > 999 уже не выполняется
#     ticket_number //= 10              # уменьшаем исходное число на последнюю отработанную цифру

# print(f"The ticket is lucky: {sum_first == sum_last}")

# --------------------------Решение строками
# ticket_num = input()
# sum_first = int(ticket_num[0]) + int(ticket_num[1]) + int(ticket_num[3])
# sum_last = int(ticket_num[3]) + int(ticket_num[4]) + int(ticket_num[5])
# print(f"The ticket is lucky: {sum_first == sum_last}")