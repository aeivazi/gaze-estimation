import unittest
import numpy as np
from src.rotation_matrix import calculate_rotation_matrix_extrinsic

class TestRotateMatrix(unittest.TestCase):

    def test_calculate_rotation_matrix_extrinsic(self):

        alpha, beta, gamma = (0, 0, 0)
        expected_value = [[1, 0, 0],
                          [0, 1, 0],
                          [0, 0, 1]]
        rotation_matrix = calculate_rotation_matrix_extrinsic(alpha, beta, gamma)
        np.testing.assert_array_almost_equal(rotation_matrix, expected_value)

        alpha, beta, gamma = (90, 0, 0)
        expected_value = [[1, 0,  0],
                          [0, 0, -1],
                          [0, 1,  0]]
        rotation_matrix = calculate_rotation_matrix_extrinsic(alpha, beta, gamma)
        np.testing.assert_array_almost_equal(rotation_matrix, expected_value)

        alpha, beta, gamma = (0, 90, 0)
        expected_value = [[0,  0, 1],
                          [0,  1, 0],
                          [-1, 0, 0]]
        rotation_matrix = calculate_rotation_matrix_extrinsic(alpha, beta, gamma)
        np.testing.assert_array_almost_equal(rotation_matrix, expected_value)

        alpha, beta, gamma = (0, 0, 90)
        expected_value = [[0, -1, 0],
                          [1,  0, 0],
                          [0,  0, 1]]
        rotation_matrix = calculate_rotation_matrix_extrinsic(alpha, beta, gamma)
        np.testing.assert_array_almost_equal(rotation_matrix, expected_value)

        alpha, beta, gamma = (90, 90, 0)
        expected_value = [[0,  1, 0],
                          [0,  0, -1],
                          [-1, 0, 0]]
        rotation_matrix = calculate_rotation_matrix_extrinsic(alpha, beta, gamma)
        np.testing.assert_array_almost_equal(rotation_matrix, expected_value)

        alpha, beta, gamma = (90, 90, 90)
        expected_value = [[0,  0, 1],
                          [0,  1, 0],
                          [-1, 0, 0]]
        rotation_matrix = calculate_rotation_matrix_extrinsic(alpha, beta, gamma)
        np.testing.assert_array_almost_equal(rotation_matrix, expected_value)


if __name__ == '__main__':
    unittest.main(verbosity=1)