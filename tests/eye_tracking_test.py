import unittest
import numpy as np
from src.coordinate_system_transformations import transform_2D_to_3D, transform_3D_to_3D


class TestEyeTracking(unittest.TestCase):

    def test_transform_2D_to_3D(self):

        focal_length_cm = 1.2
        pixel_size_x_cm, pixel_size_y_cm = (0.0048, 0.0048)
        principal_point_x, principal_point_y = (400, 300)
        alpha, beta, gamma = (0, 0, 0)
        x_shift, y_shift, z_shift = (0, 0, 12)

        pupil_x, pupil_y = (340, 193)
        expected_value = (-0.288, 0.5136, 10.8)
        vector_CCS = transform_2D_to_3D(pupil_x, pupil_y, focal_length_cm, pixel_size_x_cm, pixel_size_y_cm,
                                        principal_point_x, principal_point_y)
        vector_WCS = transform_3D_to_3D(*vector_CCS, alpha, beta, gamma, x_shift, y_shift, z_shift)
        np.testing.assert_array_almost_equal(vector_WCS, expected_value)


if __name__ == '__main__':
    unittest.main(verbosity=1)