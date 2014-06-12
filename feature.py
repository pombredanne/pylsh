from enum import Enum

class Feature_Type(Enum):
    boolean = 1
    discrete = 2
    real = 3

class feature:
    def __init__(vector, feature_type)
        self.vector = vector
        self.feature_type = feature_type
