import unittest
import numpy as np

from src.calculate_point_of_interest import calculate_point_of_interest

class TestCalculateOpticAxis(unittest.TestCase):

    def test_calculate_point_of_interest(self):

        cornea_center = np.array([1.56013955, 2.50435559, 47.78392692])
        visual_axis_unit_vector = np.array([-0.296225, -0.195216, -0.934955])
        z_shift = -20

        point_of_interest = calculate_point_of_interest(cornea_center, visual_axis_unit_vector, z_shift)

        expected_value = np.array([-19.916075, -11.64874 , -20.])
        np.testing.assert_array_almost_equal(point_of_interest, expected_value)


if __name__ == '__main__':
    unittest.main()