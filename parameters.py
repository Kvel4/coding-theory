import numpy as np

from common import to_line
from hamming import hamming_dist, hamming_weight, compare_same_weight


def find_d_min_by_g_matrix(g_matrix):
    # Calculate all code words (in c_all)
    c_all = []
    for i in range(2 ** len(g_matrix)):
        word = np.array(list(format(i, f'0{len(g_matrix)}b')), dtype=int)
        word = word.dot(g_matrix)
        word %= 2
        c_all.append(word)

    # Calculate min dist (aka compare all pairs)
    d_min = len(g_matrix)
    for i in range(len(c_all)):
        for j in range(i, len(c_all), 1):
            if i != j:
                dist = hamming_dist(c_all[i], c_all[j])
                if dist < d_min:
                    d_min = dist

    return d_min


# Calculate all syndrome for each error vector by H matrix
def find_syndromes(h_source):
    h_matrix = h_source.copy()
    n = len(h_matrix[0])
    syndrome = {}
    all_code_word = []
    h_matrix = h_matrix.transpose()

    # Calculate syndrome for each error vector
    for i in range(2 ** n):
        new_word = np.array(list(format(i, f'0{n}b')), dtype=int)
        e_word = new_word.dot(h_matrix)
        e_word %= 2

        syndrome_word = int(to_line(list(e_word)), 2)
        if syndrome_word == 0:
            all_code_word.append(new_word)

        if syndrome_word not in syndrome:
            syndrome[syndrome_word] = new_word
        else:
            old_word = syndrome[syndrome_word]
            if hamming_weight(old_word) > hamming_weight(new_word):
                syndrome[syndrome_word] = new_word
            elif hamming_weight(old_word) == hamming_weight(new_word):
                syndrome[syndrome_word] = compare_same_weight(old_word, new_word)

    return syndrome


# Create standard table by H matrix
def get_standard_table(h_matrix):
    syndrome = find_syndromes(h_matrix)
    standard_table = {}

    for i in range(2 ** len(h_matrix[0])):
        binary_index = format(i, f'0{len(h_matrix[0])}b')[::-1]
        index = int(binary_index, 2)
        if index not in syndrome:
            continue
        standard_table[index] = list(syndrome[index])
    return standard_table
