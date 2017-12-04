import unittest
import numpy as np
from src.calculate_optic_axis import calculate_r, calculate_kr, calculate_iota, calculate_p, calculate_optic_axis_unit_vector


class TestCalculateOpticAxis(unittest.TestCase):

    def test_calculate_kr(self):
        camera_position_wcs = np.array([0, 0, 0])
        pupil_center_wcs = np.array([-0.03700800000000001, -0.060815999999999995, -1.2])
        center_of_cornea_curvature_wcs = np.array([1.56013955, 2.50435559, 47.78392692])
        R_const_cm = 0.78

        kr = calculate_kr(camera_position_wcs, pupil_center_wcs, center_of_cornea_curvature_wcs, R_const_cm)

        expected_value = 39.184426380438602
        self.assertAlmostEqual(kr, expected_value)

    def test_calculate_r(self):

        camera_position_wcs = np.array([0, 0, 0])
        pupil_center_wcs = np.array([-0.03700800000000001, -0.060815999999999995, -1.2])
        center_of_cornea_curvature_wcs = np.array([1.56013955, 2.50435559, 47.78392692])
        R_const_cm = 0.78

        r = calculate_r(camera_position_wcs, pupil_center_wcs, center_of_cornea_curvature_wcs, R_const_cm)

        expected_value = np.array([1.450137, 2.38304, 47.021312])
        np.testing.assert_array_almost_equal(r, expected_value)

        R = np.linalg.norm(r - center_of_cornea_curvature_wcs)
        self.assertAlmostEqual(R, R_const_cm, places=2)

    def test_calculate_iota(self):

        camera_position_wcs = np.array([0, 0, 0])
        pupil_point_refraction = np.array([1.450137, 2.38304, 47.021312])
        center_of_cornea_curvature_wcs = np.array([1.56013955, 2.50435559, 47.78392692])
        R = 0.78
        n1 = 1.3375
        n2 = 1

        iota = calculate_iota(camera_position_wcs, pupil_point_refraction, center_of_cornea_curvature_wcs, R, n1, n2)

        expected_value = np.array([0.05892, 0.07742, 0.995256])
        np.testing.assert_array_almost_equal(iota, expected_value)

    def test_calculate_p(self):

        camera_position_wcs = np.array([0, 0, 0])
        pupil_point_refraction = np.array([1.450137, 2.38304, 47.021312])
        center_of_cornea_curvature_wcs = np.array([1.56013955, 2.50435559, 47.78392692])
        R_const = 0.78
        K_const = 0.42
        n1_const = 1.3375
        n2_const = 1

        pupil_center = \
            calculate_p(camera_position_wcs,
                        pupil_point_refraction,
                        center_of_cornea_curvature_wcs,
                        R_const, K_const, n1_const, n2_const)

        expected_value = np.array([1.471612,   2.411258,  47.384058])
        np.testing.assert_array_almost_equal(pupil_center, expected_value)

        K = np.linalg.norm(pupil_center - center_of_cornea_curvature_wcs)
        self.assertAlmostEqual(K, K_const, places=2)

    def test_calculate_optic_axis_unit_vector(self):

        camera_position_wcs = np.array([0, 0, 0])
        pupil_center_wcs = np.array([-0.03700800000000001, -0.060815999999999995, -1.2])
        cornea_center = np.array([1.56013955, 2.50435559, 47.78392692])
        R_const = 0.78
        K_const = 0.42
        n1_const = 1.3375
        n2_const = 1

        omega = \
            calculate_optic_axis_unit_vector(pupil_center_wcs, camera_position_wcs, cornea_center, R_const, K_const, n1_const, n2_const)

        expected_value = np.array([-0.210779, -0.221661, -0.952071])
        np.testing.assert_array_almost_equal(omega, expected_value)

        self.assertAlmostEqual(np.linalg.norm(omega), 1)



if __name__ == '__main__':
    unittest.main()