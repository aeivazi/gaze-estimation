import unittest
import numpy as np
import math
from src.calculate_visual_axis import calculate_eye_angles, calculate_visual_axis_unit_vector, calculate_point_of_interest


class TestCalculateOpticAxis(unittest.TestCase):

    def test_calculate_eye_angles(self):

        omega = np.array([-0.210779, -0.221661, -0.952071])

        angles = calculate_eye_angles(omega)

        expected_value = np.array([-0.217876, -0.223518,  0])
        np.testing.assert_array_almost_equal(angles, expected_value)

    def test_calculate_visual_axis(self):

        optic_axis_unit_vector = np.array([-0.210779, -0.221661, -0.952071])
        alpha_right = math.radians(-5)
        beta = math.radians(1.5)

        visual_axis_unit_vector = calculate_visual_axis_unit_vector(optic_axis_unit_vector, alpha_right, beta)

        expected_value = np.array([-0.296225, -0.195216, -0.934955])
        np.testing.assert_array_almost_equal(visual_axis_unit_vector, expected_value)

        self.assertAlmostEqual(np.linalg.norm(visual_axis_unit_vector), 1)


    def test_calculate_point_of_interest(self):

        cornea_center = np.array([1.56013955, 2.50435559, 47.78392692])
        optic_axis_unit_vector = np.array([-0.210779, -0.221661, -0.952071])
        z_shift = -20
        alpha_right = math.radians(-5)
        beta = math.radians(1.5)

        point_of_interest = calculate_point_of_interest(cornea_center, optic_axis_unit_vector, z_shift, alpha_right, beta)

        expected_value = np.array([-19.916087, -11.648742, -20.])
        np.testing.assert_array_almost_equal(point_of_interest, expected_value)


if __name__ == '__main__':
    unittest.main()