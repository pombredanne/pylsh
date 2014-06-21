''' This module defines classes for generating LSH Signuture'''
import mmh3
import random

class Signuture(object):
    ''' 
    Signuture represents the Signuture of an original feature vector
    using either minhash (for boolean vector with Jaccard Similarity) 
    or random projection (continuous vector with cosine similarity)
    '''

    def __init__(self, feat, sig_len, planes=None, hash_type='minhash'):
        self.feature = feat
        self.sig_len = sig_len
        self.signuture = []
        self.planes = planes
        self.hash_type = hash_type
        random.seed(1)

    def gen_siganuture(self):
        ''' generate signuture for original feature vector'''
        if self.hash_type == 'minhash':
            self._min_hash()
        else:
            self._random_projection()

    def _min_hash(self):
        ''' Min hash for Jaccard Similarity'''
        self.signuture = [self._gen_single_bit(i) for i in xrange(self.sig_len)]

    def _gen_single_bit(self, i):
        ''' 
        a helper function for minhash
        generate single bit of signuture using ith hasher
        '''
        try:
            bit = min([mmh3.hash(str(index), i) % self.sig_len \
                for index in xrange(len(self.feature)) \
                    if self.feature[index] == 1])
            return bit
        except:
            return self.sig_len

    def _random_projection(self):
        ''' Random projection for cosine similarity'''
        if self.planes == None:
            self._gen_random_planes()
        self.signuture = [self._project(self.feature, plane) \
            for plane in self.planes]

    @staticmethod
    def _project(vector, plane):
        ''' poject vector on plane, returns sign of projection '''
        assert len(vector) == len(plane)

        if Signuture._dot_product(vector, plane) >= 0:
            return 1
        return -1

    @staticmethod
    def _dot_product(vec1, vec2):
        ''' compute dot product of two vectors'''
        dot = 0.0
        for x_val, y_val in zip(vec1, vec2):
            dot += x_val * y_val
        return dot

    def _gen_random_planes(self):
        ''' Generate and stores random planes '''
        self.planes = [self._gen_random_plane(len(self.feature)) \
            for _ in xrange(self.sig_len)]

    @staticmethod
    def _gen_random_plane(dim):
        ''' generate random hyperplane with dimension dim'''
        return [random.gauss(0, 1) for _ in xrange(dim)]


class Banding:
    pass
