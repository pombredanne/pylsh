import lsh
import random
import numpy as np

def gen_random_vector(dim):
    ''' generate random vector '''
    return np.array([random.uniform(-1, 1) for _ in xrange(dim)])

def gen_random_bit_vector(dim):
    ''' generate random bit vector '''
    return np.array([int(random.uniform(-1, 1) > 0) for _ in xrange(dim)])

def test_minhash(feat_dim=5, sig_dim=1000):
    ''' test lsh for jaccard similarity'''
    
    sim = lsh.JaccardSimilarity()
    lshash = lsh.Lsh(feat_dim, sig_dim, sim)
    x = lsh.LshObject(gen_random_bit_vector(feat_dim))
    y = lsh.LshObject(gen_random_bit_vector(feat_dim)) 
    lshash.generate_signature(x)
    lshash.generate_signature(y)

    print x.feature 
    print y.feature
    print "jaccard similarity: " +\
     str(sim.compute_similarity(x.feature, y.feature))
    print "approximated similarity: " +\
     str(sim.approximate_similarity(x.signature, y.signature))

def test_random_projection(feat_dim=5, sig_dim=1000):
    ''' test lsh for cosine similarity'''
    
    sim = lsh.CosineSimilarity()
    lshash = lsh.Lsh(feat_dim, sig_dim, sim)
    x = lsh.LshObject(gen_random_vector(feat_dim))
    y = lsh.LshObject(gen_random_vector(feat_dim)) 
    lshash.generate_signature(x)
    lshash.generate_signature(y)

    print x.feature 
    print y.feature
    print "cosine similarity: " + \
        str(sim.compute_similarity(x.feature, y.feature))
    print "approximated similarity: " + \
        str(sim.approximate_similarity(x.signature, y.signature))

def test_index_retrieval(feat_dim=10, sig_dim=100):
    '''Test lsh index and retrieval'''
    sim = lsh.JaccardSimilarity()
    lshash = lsh.Lsh(feat_dim, sig_dim, sim)
    for _ in xrange(100):
        lshash.index(lsh.LshObject(gen_random_bit_vector(feat_dim)))

    for _ in xrange(5):
        obj = lsh.LshObject(gen_random_bit_vector(feat_dim))
        results = lshash.retrieve(obj)
        print "Data retrieved for %s:" % obj
        for result in results:
            print result

if __name__ == '__main__':
    test_random_projection()
    test_minhash()
    test_index_retrieval()


