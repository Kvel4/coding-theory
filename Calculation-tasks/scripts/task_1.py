import numpy as np

from matrixreductions import evaluate_num
from parameters import find_d_min_by_g_matrix, find_syndromes
from common import to_line
from gauss import gauss, gauss_minimize
from read import read_matrix


# @author Geny200
# @version 3.8
# Sorry for the code, I don't write on python.


# Makes the calculation of the generating matrix (G)
# and related parameters (n and k).
# This function takes into account the conditions of
# minimality of the column numbers of the E matrix in G.
def rz_task(file_name, logger):
    h_matrix = []
    with open(file_name, 'r') as reader:
        h_matrix = read_matrix(reader)

    if not h_matrix or len(h_matrix) > len(h_matrix[0]):
        logger('err: Smth wrong with matrix;')
        return

    h_matrix = np.array(h_matrix, dtype=int)
    h_source = h_matrix.copy()

    rank = np.linalg.matrix_rank(h_matrix)
    n = len(h_matrix[0])
    k = n - rank
    logger(f'n = {n}\nk = {n - rank}')

    if rank != len(h_matrix) or len(h_matrix[0]) != rank * 2:
        logger('warning: There might be mistake;')

    # Some hack for minimality conditions
    for i in range(len(h_matrix[0])):
        h_matrix[:, i] = np.flip(h_matrix[:, i])
    for i in range(len(h_matrix)):
        h_matrix[i] = np.flip(h_matrix[i])

    # Evaluate I and A
    h_matrix, swap_buff = gauss(h_matrix)

    # Some hack for minimality conditions
    for i in range(len(h_matrix)):
        h_matrix[i] = np.flip(h_matrix[i])
    for i in range(len(h_matrix[0])):
        h_matrix[:, i] = np.flip(h_matrix[:, i])

    # Change index of columns (because of .flip())
    swap_buff = evaluate_num(n, swap_buff)
    swap_buff.reverse()

    a_t = h_matrix[:len(h_matrix), :len(h_matrix)].copy()

    # Create G matrix
    g_matrix = np.zeros([len(h_matrix), len(h_matrix[0])], dtype=int)
    g_matrix[:, len(g_matrix):] = a_t.transpose()
    g_matrix[:, :len(g_matrix)] = np.eye(len(g_matrix), len(g_matrix), dtype=int)

    # Swap columns
    for l, r in swap_buff:
        copy = g_matrix[:, l].copy()
        g_matrix[:, l] = g_matrix[:, r]
        g_matrix[:, r] = copy

    # Make minimal G
    g_matrix = gauss_minimize(g_matrix)

    # Show answers
    logger(f'H = \n{h_source}')
    logger(f'G = \n{g_matrix}')

    copyable_show = to_line(
        list(
            to_line(y) for y in list(g_matrix)
        ), '\n'
    )
    logger(f'G = \n{copyable_show}')

    g_dot_ht = g_matrix.dot(h_source.transpose())
    g_dot_ht %= 2
    logger(f'Check G * H = \n{g_dot_ht}')

    # Calculate all code words and evaluate d_min
    d_min = find_d_min_by_g_matrix(g_matrix)
    logger(f'd_min = {d_min}')

    syndrome = find_syndromes(h_source)

    # logger standard table
    for i in range(2 ** len(h_source)):
        binary_index = format(i, f'0{len(h_source)}b')[::-1]
        index = int(binary_index, 2)
        if index not in syndrome:
            logger('')
            continue
        logger(f'T[{binary_index}] = {to_line(list(syndrome[index]))}')


# Evaluate task from file
# !! Input file must not contain extra lines
if __name__ == '__main__':
    rz_task('data/task_1.txt', print)
