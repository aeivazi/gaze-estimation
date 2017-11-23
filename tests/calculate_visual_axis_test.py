import unittest
import numpy as np
import math
from src.calculate_visual_axis import calculate_eye_angles, calculate_point_of_interest


class TestCalculateOpticAxis(unittest.TestCase):

    def test_calculate_eye_angles(self):

        omega = np.array([-0.24600787, 0.03989999, 0.96844624])

        angles = calculate_eye_angles(omega)

        expected_value = np.array([0.24876166054830931, 0.039910584450204276, 0])
        np.testing.assert_array_almost_equal(angles, expected_value)

    def test_calculate_point_of_interest(self):

        c = np.array([1.46826769, 1.99285342, 48.37022867])
        optic_axis_unit_vector= np.array([-0.24600787, 0.03989999, 0.96844624])
        z_shift = -20
        alpha_right = math.radians(-5)
        beta = math.radians(1.5)

        point_of_interest = calculate_point_of_interest(c, optic_axis_unit_vector, z_shift, alpha_right, beta)
        print(point_of_interest)

        expected_value = np.array([12.595469, 6.567024, -20])
        np.testing.assert_array_almost_equal(point_of_interest, expected_value)


if __name__ == '__main__':
    unittest.main()