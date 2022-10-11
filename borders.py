import math


def choose(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0


def hamming_border(d, n, k):
    m = 2 ** k
    upper = 2 ** n
    bottom = 0
    for i in range(math.trunc((d - 1) / 2) + 1):
        bottom = bottom + choose(n, i)
    return m <= upper / bottom


def vg_border(d, n, k):
    qn = 2 ** (n - k)
    right = 0
    for i in range(d - 1):
        right = right + choose(n - 1, i)
    return qn > right


def griesmer_border(d, n, k):
    right = 0
    for i in range(k):
        right += math.ceil(d / 2 ** i)
    return n >= right


if __name__ == "__main__":
    n2 = 12
    d2 = 5
    n1 = 19
    k1 = 9


    for i in range(100, 1, -1):
        if hamming_border(d2, n2, i):
            print("hbd:", i)
            break

    for i in range(100, 1, -1):
        if griesmer_border(d2, n2, i):
            print("gbd:", i)
            break

    for i in range(100, 1, -1):
        if vg_border(d2, n2, i):
            print("vgbd:", i)
            break


    for i in range(100, 1, -1):
        if hamming_border(i, n1, k1):
            print("hb:", i)
            break

    for i in range(100, 1, -1):
        if griesmer_border(i, n1, k1):
            print("gb:", i)
            break


    for i in range(100, 1, -1):
        if vg_border(i, n1, k1):
            print("vgb:", i)
            break