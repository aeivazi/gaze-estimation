import numpy as np


def calculate_magnitude(a):
    return np.sqrt(a.dot(a))


def normalize(a):
    return a/calculate_magnitude(a)