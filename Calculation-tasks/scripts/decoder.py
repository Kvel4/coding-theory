from matrixreductions import get_H_matrix_by_G
from parameters import get_standard_table
from common import to_line



def decode_by_h_matrix(h_matrix, Y):
    matrix = h_matrix.copy()
    standard_table = get_standard_table(matrix)
    syndrome = Y.dot(matrix.transpose())
    syndrome %= 2
    code_word = list(map(lambda x, y: (x + y) % 2, list(Y), list(standard_table[int(to_line(list(syndrome)), 2)])))

    return code_word


def decode_by_g_matrix(g_matrix, Y):
    return decode_by_h_matrix(get_H_matrix_by_G(g_matrix), Y)
