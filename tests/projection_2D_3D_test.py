import unittest
import numpy as np
from src.projection_2D_3D import project_2D_to_3D, project_3D_to_2D


class Test2D3DProjection(unittest.TestCase):

    def test_project_2D_to_3D(self):

        focal_length_cm = 1.2
        pixel_size_x_cm, pixel_size_y_cm = (0.0048, 0.0048)
        camera_monitor_distance = 12
        principal_point_x, principal_point_y = (400, 300)

        x, y = (400, 300)
        expected_value = (0, 0 , 12)
        vector_3D = project_2D_to_3D(x, y, focal_length_cm, pixel_size_x_cm, pixel_size_y_cm,
                                     principal_point_x, principal_point_y, camera_monitor_distance)
        np.testing.assert_array_almost_equal(vector_3D, expected_value)

        x, y = (400, 425)
        expected_value = (0, 6, 12)
        vector_3D = project_2D_to_3D(x, y, focal_length_cm, pixel_size_x_cm, pixel_size_y_cm,
                                     principal_point_x, principal_point_y, camera_monitor_distance)
        np.testing.assert_array_almost_equal(vector_3D, expected_value)

        x, y = (400, 425)
        expected_value = (0, 6, 12)
        vector_3D = project_2D_to_3D(x, y, focal_length_cm, pixel_size_x_cm, pixel_size_y_cm,
                                     principal_point_x, principal_point_y, camera_monitor_distance)
        np.testing.assert_array_almost_equal(vector_3D, expected_value)

        x, y = (650, 425)
        expected_value = (12, 6, 12)
        vector_3D = project_2D_to_3D(x, y, focal_length_cm, pixel_size_x_cm, pixel_size_y_cm,
                                     principal_point_x, principal_point_y, camera_monitor_distance)
        np.testing.assert_array_almost_equal(vector_3D, expected_value)

        x, y = (150, 425)
        expected_value = (-12, 6, 12)
        vector_3D = project_2D_to_3D(x, y, focal_length_cm, pixel_size_x_cm, pixel_size_y_cm,
                                     principal_point_x, principal_point_y, camera_monitor_distance)
        np.testing.assert_array_almost_equal(vector_3D, expected_value)

        x, y = (150, 175)
        expected_value = (-12, -6, 12)
        vector_3D = project_2D_to_3D(x, y, focal_length_cm, pixel_size_x_cm, pixel_size_y_cm,
                                     principal_point_x, principal_point_y, camera_monitor_distance)
        np.testing.assert_array_almost_equal(vector_3D, expected_value)

        x, y = (0, 0)
        expected_value = (-19.2, -14.4, 12)
        vector_3D = project_2D_to_3D(x, y, focal_length_cm, pixel_size_x_cm, pixel_size_y_cm,
                                     principal_point_x, principal_point_y, camera_monitor_distance)
        np.testing.assert_array_almost_equal(vector_3D, expected_value)

        x, y = (800, 600)
        expected_value = (19.2, 14.4, 12)
        vector_3D = project_2D_to_3D(x, y, focal_length_cm, pixel_size_x_cm, pixel_size_y_cm,
                                     principal_point_x, principal_point_y, camera_monitor_distance)
        np.testing.assert_array_almost_equal(vector_3D, expected_value)

    def test_project_3D_to_2D(self):

        focal_length_cm = 1.2
        pixel_size_x_cm, pixel_size_y_cm = (0.0048, 0.0048)
        principal_point_x, principal_point_y = (400, 300)

        x, y, z = (0, 0, 12)
        expected_value = (400, 300)
        vector_2D = project_3D_to_2D(x, y, z, focal_length_cm, pixel_size_x_cm, pixel_size_x_cm,
                                     principal_point_x, principal_point_y)
        np.testing.assert_array_almost_equal(vector_2D, expected_value)

        x, y, z = (0, 6, 12)
        expected_value = (400, 425)
        vector_2D = project_3D_to_2D(x, y, z, focal_length_cm, pixel_size_x_cm, pixel_size_x_cm,
                                     principal_point_x, principal_point_y)
        np.testing.assert_array_almost_equal(vector_2D, expected_value)

        x, y, z = (12, 6, 12)
        expected_value = (650, 425)
        vector_2D = project_3D_to_2D(x, y, z, focal_length_cm, pixel_size_x_cm, pixel_size_x_cm,
                                     principal_point_x, principal_point_y)
        np.testing.assert_array_almost_equal(vector_2D, expected_value)

        x, y, z = (-12, 6, 12)
        expected_value = (150, 425)
        vector_2D = project_3D_to_2D(x, y, z, focal_length_cm, pixel_size_x_cm, pixel_size_x_cm,
                                     principal_point_x, principal_point_y)
        np.testing.assert_array_almost_equal(vector_2D, expected_value)

        x, y, z = (-12, -6, 12)
        expected_value = (150, 175)
        vector_2D = project_3D_to_2D(x, y, z, focal_length_cm, pixel_size_x_cm, pixel_size_x_cm,
                                     principal_point_x, principal_point_y)
        np.testing.assert_array_almost_equal(vector_2D, expected_value)

        x, y, z = (-19.2, -14.4, 12)
        expected_value = (0, 0)
        vector_2D = project_3D_to_2D(x, y, z, focal_length_cm, pixel_size_x_cm, pixel_size_x_cm,
                                     principal_point_x, principal_point_y)
        np.testing.assert_array_almost_equal(vector_2D, expected_value)

        x, y, z = (19.2, 14.4, 12)
        expected_value = (800, 600)
        vector_2D = project_3D_to_2D(x, y, z, focal_length_cm, pixel_size_x_cm, pixel_size_x_cm,
                                     principal_point_x, principal_point_y)
        np.testing.assert_array_almost_equal(vector_2D, expected_value)


if __name__ == '__main__':
    unittest.main(verbosity=1)