import unittest
import numpy as np

from src.calculate_point_of_interest import calculate_point_of_interest, transform_to_screen_coordinate_system


class TestCalculateOpticAxis(unittest.TestCase):

    def test_screen_coord_system_transform(self):

        cornea_center_of_curvature = np.array([1.56013955, 2.50435559, 47.78392692])
        visual_axis_unit_vector = np.array([-0.296225, -0.195216, -0.934955])
        camera_rotation_angles = np.radians(np.array([0, 0, 0]))

        cornea_center_of_curvature_scs, visual_axis_unit_vector_scs  = \
            transform_to_screen_coordinate_system(cornea_center_of_curvature, visual_axis_unit_vector, camera_rotation_angles)

        np.testing.assert_array_almost_equal(cornea_center_of_curvature_scs, cornea_center_of_curvature)
        np.testing.assert_array_almost_equal(visual_axis_unit_vector_scs, visual_axis_unit_vector)

        camera_rotation_angles = np.radians(np.array([8, 0, 0]))

        cornea_center_of_curvature_scs, visual_axis_unit_vector_scs = \
            transform_to_screen_coordinate_system(cornea_center_of_curvature, visual_axis_unit_vector,
                                                  camera_rotation_angles)

        np.testing.assert_array_almost_equal(cornea_center_of_curvature_scs, np.array([1.560139, -4.170254,  47.667436]))
        np.testing.assert_array_almost_equal(visual_axis_unit_vector_scs, np.array([-0.296225, -0.063196, -0.953025]))

    def test_calculate_point_of_interest(self):

        cornea_center = np.array([1.560139, 2.387901, 47.789887])
        visual_axis_unit_vector = np.array([-0.296225, -0.192936, -0.935427])
        z_shift = -20

        point_of_interest = calculate_point_of_interest(cornea_center, visual_axis_unit_vector, z_shift)

        expected_value = np.array([-19.907126, -11.594066, -20.])
        np.testing.assert_array_almost_equal(point_of_interest, expected_value)


if __name__ == '__main__':
    unittest.main()