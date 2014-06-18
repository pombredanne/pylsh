''' This module defines classes for generating LSH Siganuture'''
class Siganuture(object):
    ''' 
    Siganuture represents the siganuture of an original feature vector
    using either minhash (for boolean vector with Jaccard Similarity) 
    or random projection (continuous vector with cosine similarity)
    '''
    def __init__(self, feat, sig_len, hasher):
        self.feature = feat
        self.sig_len = sig_len
        self.hasher = hasher
        self.signuture = []

    def gen_siganuture(self):
        ''' generate siganuture for original feature vector'''
        self._min_hash()

    def _min_hash(self):
        ''' Min hash for Jaccard Similarity'''
        for i in xrange(self.sig_len):
            self.signuture.append(self._gen_single_bit(i))


    def _gen_single_bit(self, i):
        ''' 
        a helper function for minhash
        generate single bit of signuture using ith hasher
        '''
        return min([self.hasher.hash(index, i) % self.sig_len \
            for index in xrange(len(self.feature)) if self.feature[index] == 1])

    def _random_projection(self):
        ''' Random projection for cosine similarity'''
        pass

class Hasher(object):
    ''' Hasher defines method to generate a family of hash function '''
    def __init__(self, num):
        import random
        self.num = num
        self.hashes = [random.getrandbits(32) for _ in xrange(num)]

    def hash(self, obj, i):
        ''' 
        Generate hash using ith hash function,
        returns the hash value using ith hash functions
        '''
        assert i < self.num
        return hash(obj) ^ self.hashes[i]

class Banding:
    pass
