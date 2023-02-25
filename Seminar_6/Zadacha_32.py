# ДЗ. Задача 32: 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from Module_for_30_32 import create_list, indexes_of_numbers

num_list = create_list(int(input('Введите размер массива: ')))
left_endpoint = int(input('Введите минимум диапазона: '))
right_endpoint = int(input('Введите максимум диапазона: '))

print(*num_list)
print(*indexes_of_numbers(num_list, left_endpoint, right_endpoint))