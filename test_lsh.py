import lsh
import random
import math

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

    if union == 0:
        union = 1

    return 1.0 * join / union

def approximate_jaccard(vec1, vec2):
    ''' compute approximated jaccard similarity '''
    assert len(vec1) == len(vec2)
    count = 0

    for x_bit, y_bit in zip(vec1, vec2):
        if x_bit == y_bit:
            count += 1

    return 1.0 * count / len(vec1)

def cosine_similarity(vec1, vec2):
    ''' compute cosine similarity of vector vec1 and vec2 '''
    return dot_product(vec1, vec2) / vector_length(vec1) / vector_length(vec2)

def approximate_cosine(vec1, vec2):
    ''' approximated cosine similarity on random projected signuture '''
    return math.cos(math.pi  * (1 - approximate_jaccard(vec1, vec2)))

def vector_length(vec):
    ''' normalize vector x '''
    return math.sqrt(sum([val * val for val in vec]))


def dot_product(vec1, vec2):
    ''' compute dot product of vector x and y '''
    dot = 0
    for x_val, y_val in zip(vec1, vec2):
        dot += x_val * y_val
    return dot

def gen_random_vector(dim):
    ''' generate random vector '''
    return [random.uniform(-1, 1) for _ in xrange(dim)]

def gen_random_bit_vector(dim):
    ''' generate random bit vector '''
    return [int(random.uniform(-1, 1) > 0) for _ in xrange(dim)]

def test_minhash():
    ''' test lsh for jaccard similarity'''
    reload(random)
    x = gen_random_bit_vector(5)
    y = gen_random_bit_vector(5)
    sig_len = 100

    x_sig = lsh.Signuture(x, sig_len)
    y_sig = lsh.Signuture(y, sig_len)
    x_sig.gen_siganuture()
    y_sig.gen_siganuture()

    print "jaccard similarity: " + str(jaccard_similarity(x, y))
    print "approximated similarity: " + \
        str(approximate_jaccard(x_sig.signuture, y_sig.signuture))

def test_random_projection():
    ''' test lsh for cosine similarity'''
    reload(random)
    x = gen_random_vector(4)
    y = gen_random_vector(4)
    sig_len = 1000
    x_sig = lsh.Signuture(x, sig_len, hash_type='random_projection')
    x_sig.gen_siganuture()
    y_sig = lsh.Signuture(y, sig_len, hash_type='random_projection')
    y_sig.gen_siganuture()

    print "cosine similarity: " + str(cosine_similarity(x, y))
    print "approximated similarity: " + \
        str(approximate_cosine(x_sig.signuture, y_sig.signuture))


if __name__ == '__main__':
    test_random_projection()
    test_minhash()


