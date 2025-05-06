# Abdelrahman Othman
# 6-5-2025

import numpy as np


def calculate_similarity_score(file_path='input.txt'):
    """
    Calculate the similarity score of a given input file.
    :param file_path:
    :return: similarity score
    """
    left_col = []
    right_col = []
    result = 0
    with open('input.txt') as f:
        for line in f:
            splited_line = line.split("   ")
            right_col.append(int(splited_line[0].strip()))
            left_col.append(int(splited_line[1].strip()))

    left_col = np.array(sorted(left_col))
    right_col = np.array(sorted(right_col))

    for num in left_col:
        result += np.count_nonzero(right_col == num) * num
    return result


if __name__ == '__main__':
    print(calculate_similarity_score())
