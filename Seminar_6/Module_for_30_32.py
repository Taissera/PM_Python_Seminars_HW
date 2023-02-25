def arithmetic_sequence(a1: int, a_diff: int, n: int):
    sequence = [a1]
    for i in range(2, n + 1):
        sequence.append(a1 + (i - 1) * a_diff)
    return sequence


def create_list(x: int):
    my_list = []
    for _ in range(x):
        my_list.append(int(input('Введите число: ')))
    return my_list


def indexes_of_numbers(num_lst: list, start: int, end: int):
    indexes_list = []
    for i in range(len(num_lst)):
        if start <= num_lst[i] <= end:
            indexes_list.append(i)
    return indexes_list
