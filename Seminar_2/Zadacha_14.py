# Задача 14.
# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8


N = int(input("Введите значение числа N: "))
k = 1
while k < N:
    if (k < N):
        if (k * 2 > N):
            break
        else:
            k = k * 2
            print(k)


# Разбор ДЗ на семинаре:

n = int(input())
pow_two = 1

while pow_two <= n:
    print(pow_two, end=" ")
    pow_two *= 2
    
    

N = int(input("Введите значение числа N: "))
k = 1
while k <= N:
    print(k)
    k = k * 2
            