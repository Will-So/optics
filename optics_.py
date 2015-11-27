import numpy as np

from sklearn.base import BaseEstimator, ClusterMixin
from sklearn.metrics import pairwise_distances
from sklearn.utils import check_random_state, check_array, check_consistent_length
from sklearn.neighbors import NearestNeighbors


def optics():
    """

    :return:
    """


class OPTICS(BaseEstimator, ClusterMixin):
    """
    Perform OPTICS clustering from a vector array or distance matrix

    OPTICS
    """