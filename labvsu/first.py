# Лабораторная работа №1
# Input: мартрица MxN
# Output: одномерный массив с номерами тех строк матрицы где есть одинаковые элементы
# Если таких строк нет, вывести соответствующее сообщение


import sys


def fill_matrix_from_file():
    with open('res/matrix.txt') as f:
        matrix = [list(map(float, row.split())) for row in f.readlines()]
    return matrix


def fill_matrix_from_keyboard():
    matrix = [list(map(float, line.split())) for line in sys.stdin]
    return matrix


def check(array):
    if not array:
        print("There is no twins")
    else:
        print(array)


def twins_set(matrix):

    columns_with_twins = []

    for i in range(len(matrix)):
        if len(set(matrix[i])) < len(matrix[i]):
            columns_with_twins.append(i)
    print(matrix)
    check(columns_with_twins)


def twins_sort(matrix):

    columns_with_twins = []

    for i in range(len(matrix)):
        matrix[i].sort()
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] == matrix[i][j + 1]:
                columns_with_twins.append(i)
                break

    check(columns_with_twins)

