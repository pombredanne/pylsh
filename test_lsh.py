import lsh

X = [0, 1, 0, 1, 0, 1]
Y = [1, 0, 0, 1, 0, 1]

SIG_LEN = 5000

def jaccard_similarity(x, y):
    ''' compute jaccard similarty betweeen x and y '''
    assert len(x) == len(y)
    join = 0
    union = 0
    for x_bit, y_bit in zip(x, y):
        if x_bit == 1 and y_bit == 1:
            join += 1

        if x_bit == 1 or y_bit == 1:
            union += 1

    return 1.0 * join / union

def approximate_jaccard(x, y):
    ''' compute approximated jaccard similarity '''
    assert len(x) == len(y)
    count = 0

    for x_bit, y_bit in zip(x, y):
        if x_bit == y_bit:
            count += 1

    return 1.0 * count / len(x)

if __name__ == '__main__':
    hasher = lsh.Hasher(SIG_LEN)
    x_sig = lsh.Siganuture(X, SIG_LEN, hasher)
    y_sig = lsh.Siganuture(Y, SIG_LEN, hasher)
    x_sig.gen_siganuture()
    y_sig.gen_siganuture()

    print "jaccard similarity: " + str(jaccard_similarity(X, Y))
    print "approximated similarity: " + \
        str(approximate_jaccard(x_sig.signuture, y_sig.signuture))



