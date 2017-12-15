import unittest
import numpy as np

from src.coordinate_system_transformations import transform_2D_to_3D, transform_3D_to_3D


class TestCSTransformation(unittest.TestCase):

    def test_transform_2D_to_3D(self):

        focal_length_cm = 1.2
        pixel_size_x_cm, pixel_size_y_cm = (0.0048, 0.0048)
        principal_point_x, principal_point_y = (400, 300)

        x, y = (400, 300)
        expected_value = (0, 0 , -1.2)
        vector_3D = transform_2D_to_3D(x, y, focal_length_cm, pixel_size_x_cm, pixel_size_y_cm,
                                       principal_point_x, principal_point_y)
        np.testing.assert_array_almost_equal(vector_3D, expected_value)

        x, y = (400, 425)
        expected_value = (0, 0.6, -1.2)
        vector_3D = transform_2D_to_3D(x, y, focal_length_cm, pixel_size_x_cm, pixel_size_y_cm,
                                       principal_point_x, principal_point_y)
        np.testing.assert_array_almost_equal(vector_3D, expected_value)

        x, y = (650, 300)
        expected_value = (1.2, 0, -1.2)
        vector_3D = transform_2D_to_3D(x, y, focal_length_cm, pixel_size_x_cm, pixel_size_y_cm,
                                       principal_point_x, principal_point_y)
        np.testing.assert_array_almost_equal(vector_3D, expected_value)

        x, y = (650, 425)
        expected_value = (1.2, 0.6, -1.2)
        vector_3D = transform_2D_to_3D(x, y, focal_length_cm, pixel_size_x_cm, pixel_size_y_cm,
                                       principal_point_x, principal_point_y)
        np.testing.assert_array_almost_equal(vector_3D, expected_value)

        x, y = (150, 175)
        expected_value = (-1.2, -0.6, -1.2)
        vector_3D = transform_2D_to_3D(x, y, focal_length_cm, pixel_size_x_cm, pixel_size_y_cm,
                                       principal_point_x, principal_point_y)
        np.testing.assert_array_almost_equal(vector_3D, expected_value)

        x, y = (0, 0)
        expected_value = (-1.92, -1.44, -1.2)
        vector_3D = transform_2D_to_3D(x, y, focal_length_cm, pixel_size_x_cm, pixel_size_y_cm,
                                       principal_point_x, principal_point_y)
        np.testing.assert_array_almost_equal(vector_3D, expected_value)

        x, y = (800, 600)
        expected_value = (1.92, 1.44, -1.2)
        vector_3D = transform_2D_to_3D(x, y, focal_length_cm, pixel_size_x_cm, pixel_size_y_cm,
                                       principal_point_x, principal_point_y)
        np.testing.assert_array_almost_equal(vector_3D, expected_value)

    def test_transform_3D_to_3D(self):
        input = np.array([0, 0, 0])
        alpha, beta, gamma = np.radians((0, 0, 0))
        shift = np.array([0, 0, -12])
        expected_value = np.array([0, 0, -12])
        output = transform_3D_to_3D(input, alpha, beta, gamma, shift)
        np.testing.assert_array_almost_equal(output, expected_value)

        input = np.array([12, 6, 12])
        alpha, beta, gamma = np.radians((0, 0, 0))
        shift = np.array([0, 0, -12])
        expected_value = np.array([12, 6, 0])
        output = transform_3D_to_3D(input, alpha, beta, gamma, shift)
        np.testing.assert_array_almost_equal(output, expected_value)

        input = np.array([12, 6, 12])
        alpha, beta, gamma = np.radians((90, 0, 0))
        shift = np.array([0, 0, 0])
        expected_value = np.array([12., -12.,   6.])
        output = transform_3D_to_3D(input, alpha, beta, gamma, shift)
        np.testing.assert_array_almost_equal(output, expected_value)

        input = np.array([12, 6, 24])
        alpha, beta, gamma = np.radians((90, 90, 90))
        shift = np.array([0, 0, 0])
        expected_value = np.array([24, 6, -12])
        output = transform_3D_to_3D(input, alpha, beta, gamma, shift)
        np.testing.assert_array_almost_equal(output, expected_value)

        input = np.array([12, 6, 24])
        alpha, beta, gamma = np.radians((90, 90, 90))
        shift = np.array([5, -10, 10])
        expected_value = np.array([29, -4, -2])
        output = transform_3D_to_3D(input, alpha, beta, gamma, shift)
        np.testing.assert_array_almost_equal(output, expected_value)


if __name__ == '__main__':
    unittest.main(verbosity=1)