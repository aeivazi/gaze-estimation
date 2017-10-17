import unittest
import numpy as np
from src.calculate_cornea_center import calculate_cornea_center_wcs
from src.coordinate_system_transformations import transform_2D_to_3D


class TestCalculateC(unittest.TestCase):

    def test_calculate_c(self):

        glint_1_ics = (333, 197)
        glint_2_ics = (315, 197)

        light_1_wcs = np.array([-23, 0, 0])
        light_2_wcs = np.array([23, 0, 0])

        camera_position_wcs = np.array([0, 0, 0])

        focal_length_cm = 1.2
        pixel_size_cm = (0.00048, 0.00048)
        principal_point = (400, 300)

        glint_1_wcs = transform_2D_to_3D(*glint_1_ics, focal_length_cm, *pixel_size_cm, *principal_point)
        glint_2_wcs = transform_2D_to_3D(*glint_2_ics, focal_length_cm, *pixel_size_cm, *principal_point)

        R_const_cm = 7.8 / 10
        distance_to_camera_cm = 55

        Kq1_init = distance_to_camera_cm/focal_length_cm
        Kq2_init = distance_to_camera_cm/focal_length_cm

        c = calculate_cornea_center_wcs(glint_1_wcs, glint_2_wcs,
                                        camera_position_wcs,
                                        light_1_wcs, light_2_wcs,
                                        R_const_cm,
                                        (Kq1_init, Kq2_init))

        expected_value = np.array([1.468268, 1.99285342, 48.37022869])
        np.testing.assert_array_almost_equal(c, expected_value)

if __name__ == '__main__':
    unittest.main()