# Abdelrahman Othman
# 6-5-2025

import numpy as np


def calculate_column_difference(file_path='input.txt'):
    """
    Calculates the difference between columns of an input file.
    :param file_path:
    :return: sum difference between columns of an input file.
    """
    left_col = []
    right_col = []

    with open('input.txt') as f:
        for line in f:
            splited_line = line.split("   ")
            right_col.append(int(splited_line[0].strip()))
            left_col.append(int(splited_line[1].strip()))

    left_col = np.array(sorted(left_col))
    right_col = np.array(sorted(right_col))

    result = np.sum(abs(right_col - left_col))
    return result


if __name__ == '__main__':
    print(calculate_column_difference())
