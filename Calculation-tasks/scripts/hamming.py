# Calculate number of '1'.
def hamming_weight(word):
    result = 0
    for i in word:
        if i > 0:
            result += 1
    return result


# Calculate number of different digit in
# the same position.
def hamming_dist(left, right):
    result = 0
    for l, r in zip(left, right):
        if l != r:
            result += 1
    return result


def compare_same_weight(left, right):
    for l, r in zip(left, right):
        if l > r:
            return left
        elif r > l:
            return right
        else:
            continue
