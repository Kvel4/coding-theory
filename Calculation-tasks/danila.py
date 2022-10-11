from collections import defaultdict
from operator import itemgetter

import numpy as np

# Constants
N, K = 10, 5

# Проверочная матрица H:
H = """1 0 0 0 1 1 0 1 0 0
 1 0 1 0 0 1 1 0 1 1
 0 0 0 1 0 1 1 0 0 0
 1 1 1 0 1 1 1 1 1 0
 1 1 1 1 0 0 0 0 0 0"""

# Идем на сайт: https://www.di-mgt.com.au/cgi-bin/matrix_stdform.cgi
# Выбираем пункт: H -> [B | In-k]
# Получаем нашу матрицу G (P.S если не получается получить матрицу с помощью сайта необходимо поменять некоторые столбцы
# в случайном порядке и потом вернуть поменянные столбцы назад
G = """1 0 0 1 0 0 1 1 1 1
 0 1 0 1 0 0 1 0 0 1
 0 0 1 1 0 0 1 0 0 0
 0 0 0 0 1 0 0 1 0 0
 0 0 0 0 0 1 1 1 1 1"""

G = list(map(lambda x: list(map(int, x.split())), G.split('\n')))
H = list(map(lambda x: list(map(int, x.split())), H.split('\n')))

H = np.array(H)
G = np.array(G)

print(f'Check if correct: {G @ H.T % 2}', end='\n\n')


# страница 50 учебника Кудряшева (𝑑 = min 𝑤 * (𝑚 * 𝐺). m != 0)
def find_min_d(k, matrix_G):
    min_d = k + 1
    for i in range(1, 2 ** k):
        bin_num = np.array(list(np.binary_repr(i).zfill(k))).astype(np.int8)
        min_d = min(np.sum(bin_num @ matrix_G % 2), min_d)

    return min_d


def find_syndromes(n, H_transpose):
    syndrome = defaultdict(lambda: 2 ** (n + 1))
    for i in range(0, 2 ** n):
        c = np.array(list(np.binary_repr(i).zfill(n))).astype(np.int8)
        word = c @ H_transpose % 2
        ind = sum(val * 2 ** index for index, val in enumerate(reversed(word)))

        syndrome[ind] = c if np.sum(c) <= np.sum(syndrome[ind]) else syndrome[ind]

    return syndrome


print(f'Min D: {find_min_d(K, G)}', end='\n\n')
syndrome_list = find_syndromes(N, H.T).items()
syndrome_list = sorted(syndrome_list, key=itemgetter(0))

mapping = {
    f"{np.binary_repr(index).zfill(K)}": f"{''.join(map(str, syndrome))}" for index, syndrome in syndrome_list
}

print('List of syndromes: ')
for index, syndrome in syndrome_list:
    key = f"{np.binary_repr(index).zfill(K)}"
    key = key[::-1]
    print(f'{key}  --->  {mapping[key]}')