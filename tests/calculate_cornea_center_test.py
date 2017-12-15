import unittest
import numpy as np
import math
from src.calculate_cornea_center import calculate_cornea_center, calculate_q, normalized, calculate_c

class TestCalculateC(unittest.TestCase):

    def test_normalize(self):
        vector = np.array([2, 2, 2])
        vector_norm = normalized(vector)
        expected_value = np.array([0.57735027, 0.57735027, 0.57735027])
        np.testing.assert_array_almost_equal(vector_norm, expected_value)

    def test_calculate_q(self):
        kq = 55
        camera_position_wcs = np.array([0, 0, 0])
        glint_wcs = np.array([-0.03482400000000001, -0.063, -1.2])

        q = calculate_q(kq, camera_position_wcs, glint_wcs)
        expected_value = np.array([1.59323602, 2.88231877, 54.90130998])
        np.testing.assert_array_almost_equal(q, expected_value)

    def test_calculate_c(self):

        camera_wcs = np.array([0, 0, 0])
        light_wcs = np.array([-23, 0, 0])
        glint_reflection_point_wcs = np.array([1.59323602, 2.88231877, 54.90130998])
        R = 0.78

        center_of_curvature = calculate_c(glint_reflection_point_wcs, light_wcs, camera_wcs, R)

        expected_value = np.array([1.76711054, 2.92218347, 55.66063761])
        np.testing.assert_array_almost_equal(center_of_curvature, expected_value)

    def test_calculate_cornea_center(self):
        constants1 = {
            'light_1_wcs': np.array([-23, 0, 0]),
            'light_2_wcs': np.array([23, 0, 0]),
            'camera_position_wcs': np.array([0, 0, 0]),
            'focal_length_cm': 1.2,
            'pixel_size_cm': (0.00048, 0.00048),
            'principal_point': (400, 300),
            'z_shift': -18,
            'alpha_right': math.radians(-5),
            'beta': math.radians(1.5),
            'R_cm': 0.95,
            'K_cm': 0.42,
            'n1': 1.3375,
            'n2': 1,
            'distance_to_camera_cm': 52,
            'camera_angle': math.radians(8)
        }

        # point4
        glint_1_ics = (327.45, 168.75)
        glint_2_ics = (309.05, 169.2)
        c = calculate_cornea_center(glint_1_ics, glint_2_ics, **constants1)
        expected_value = np.array([1.735454, 2.785454, 53.147373])
        np.testing.assert_array_almost_equal(c, expected_value)

        # point5
        glint_1_ics = (322.711, 168.816)
        glint_2_ics = (304.579, 169.211)
        c = calculate_cornea_center(glint_1_ics, glint_2_ics, **constants1)
        expected_value = np.array([1.847541,   2.806317,  53.561188])
        np.testing.assert_array_almost_equal(c, expected_value)

        # point6
        glint_1_ics = (317.78, 168.707)
        glint_2_ics = (299.561, 169.122)
        c = calculate_cornea_center(glint_1_ics, glint_2_ics, **constants1)
        expected_value = np.array([1.948963,   2.801269,  53.424463])
        np.testing.assert_array_almost_equal(c, expected_value)


if __name__ == '__main__':
    unittest.main()