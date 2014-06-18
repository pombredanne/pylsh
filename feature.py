''' This module defines the feature vector for an object '''
from enum import Enum
import abc

class Feature_Type(Enum):
    boolean = 1
    discrete = 2
    real = 3

class Feature:
    def __init__(self, vector):
        self.vector = vector

    @abc.abstractmethod
    def get_type(self):
        '''Returns the feature type of this Feature object'''
        return

class Boolean_Feature(Feature):
    def get_type(self):
        return Feature_Type.boolean

class Real_Feature(Feature):
    def get_type(self):
        return Feature_Type.real
