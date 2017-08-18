import unittest
import numpy as np
from src.vector_functions import calculate_magnitude, normalize


class TestVectorFunctions(unittest.TestCase):

    def test_calculate_magnitude(self):

        vector = np.array([1, 2, 3])
        expected_value = 3.7416573867739413

        vector_magnitude = calculate_magnitude(vector)

        self.assertAlmostEqual(vector_magnitude, expected_value)

    def test_normalize(self):
        vector = np.array([1, 2, 3])
        expected_value = np.array([0.26726124, 0.53452248, 0.80178373])

        vector_norm = normalize(vector)

        np.testing.assert_array_almost_equal(vector_norm, expected_value)


if __name__ == '__main__':
    unittest.main(verbosity=1)