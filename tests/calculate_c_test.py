import unittest
import numpy as np
from src.calculate_c import calculate_b_norm


class TestCalculateC(unittest.TestCase):

    def test_calculate_b_norm(self):

        o = np.array([0, 0, 10])
        l1 = np.array([10, -20, 0])
        l2 = np.array([-10, -20, 0])
        u1 = np.array([-1.5, 1, 8.8])
        u2 = np.array([2, 1, 8.8])

        b_norm = calculate_b_norm(o, l1, l2, u1, u2)

        expected_value = np.array([0.06451747, -0.64517472, -0.76130617])

        np.testing.assert_array_almost_equal(b_norm, expected_value)

if __name__ == '__main__':
    unittest.main()