import numpy as np


# Find first "good" column in matrix ("good" -
# means a non-zero value in the current line position;
# column index > current_row)
def find_column(matrix, current_row, current_column):
    if not matrix.any():
        return current_column

    n = len(matrix[0])
    if n <= current_column:
        return current_column

    for i in range(current_column, n):
        if np.max(matrix[current_row:, i]) > 0:
            return i
    return current_column


# Find first "good" line in matrix ("good" -
# means a non-zero value in the current column
# with the index "current_column"; row index > current_column)
def find_row(matrix, current_line, current_column):
    if not matrix.any():
        return current_line

    n = len(matrix)
    if n <= current_line:
        return current_line

    for i in range(current_line, n):
        if matrix[i, current_column] > 0:
            return i

    return current_line


# Gaussian function for constructing a I matrix in place.
def gauss(A, logger = (lambda x: x)):
    swap_buff = []
    for i in range(len(A)):
        # logger(f'-------{i}--------')
        # logger(A)
        cur = find_column(A, i, i)
        if cur != i:
            # logger(f'swap column - {i} {cur}')
            swap_buff.append((i, cur))
            copy = A[:, i].copy()
            A[:, i] = A[:, cur]
            A[:, cur] = copy
            # logger(A)
        cur = find_row(A, i, i)
        if cur != i:
            # logger(f'swap line - {i} {cur}')
            copy = A[i].copy()
            A[i] = A[cur]
            A[cur] = copy
            # logger(A)

        if i < len(A) - 1:
            for k in range(i + 1, len(A)):
                if A[k][i] > 0:
                    # logger(f'{k} - {i}')
                    A[k] -= A[i]
                    A[k] %= 2
                    # logger(f'{A}')

    for i in range(len(A), 0, -1):
        for k in range(i - 1, 0, -1):
            if A[k - 1][i - 1] > 0:
                # logger(f'{k - 1} - {i - 1}')
                A[k - 1] -= A[i - 1]
                A[k - 1] %= 2
                # logger(f'{A}')

    return A, swap_buff


# Gaussian function for minimize.
def gauss_minimize(A, reverse_traversal=True, logger = (lambda x: x)):
    columns_i_matrix = []
    column_i = 0
    for i in range(len(A)):

        cur = find_column(A, i, column_i)
        if cur != i:
            column_i = cur

        cur = find_row(A, i, column_i)
        if cur != i:
            # logger(f'swap line - {i} {cur}')
            copy = A[i].copy()
            A[i] = A[cur]
            A[cur] = copy
            # logger(A)

        if column_i < len(A[0]) - 1:
            for k in range(i + 1, len(A)):
                if A[k][column_i] > 0:
                    # logger(f'{k} - {i}')
                    A[k] -= A[i]
                    A[k] %= 2
        columns_i_matrix.append(column_i)
        column_i += 1

    if reverse_traversal:
        columns_i_matrix.reverse()
        # logger('end')
        # logger(f'{columns_i_matrix}')
        for order, column in zip(range(len(columns_i_matrix) - 1, -1, -1), columns_i_matrix):
            for row in range(order, 0, -1):
                if A[row - 1][column] > 0:
                    # logger(f'{order}, {column}, {row}')
                    # logger(f'{row - 1} - {order}')
                    A[row - 1] -= A[order]
                    A[row - 1] %= 2
                    # logger(f'{A}')

    return A
