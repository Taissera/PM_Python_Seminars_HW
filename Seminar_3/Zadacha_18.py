# ДЗ. Задача 18.
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint

list_numbers = [randint(1, 99) for _ in range(int(input("Введите размер массива: ")))]

print(list_numbers)
number = int(input("Введите число: "))
num_x = list_numbers[0]

for i in list_numbers:
    if abs(number - i) < abs(number - num_x):
        num_x = i

print(num_x)