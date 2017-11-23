import unittest
import numpy as np
from src.calculate_optic_axis import calculate_r, calculate_kr, calculate_iota, calculate_p, calculate_optic_axis_unit_vector


class TestCalculateOpticAxis(unittest.TestCase):

    def test_calculate_kr(self):

        pupil_center_wcs = np.array([-0.03216, -0.04944, -1.2])
        camera_position_wcs = np.array([0, 0, 0])
        R_const_cm = 0.78
        cornea_center_wcs = np.array([1.46826769, 1.99285342, 48.37022867])

        kr = calculate_kr(camera_position_wcs, pupil_center_wcs, cornea_center_wcs, R_const_cm)

        expected_value = 40.945611848444997
        self.assertAlmostEqual(kr, expected_value)

    def test_calculate_r(self):

        pupil_center_wcs = np.array([-0.03216, -0.04944, -1.2])
        camera_position_wcs = np.array([0, 0, 0])
        kr = 40.945611848444997

        r = calculate_r(kr, camera_position_wcs, pupil_center_wcs)

        expected_value = np.array([1.31681088, 2.02435105, 49.13473422])
        np.testing.assert_array_almost_equal(r, expected_value)

    def test_calculate_iota(self):

        camera_position_wcs = np.array([0, 0, 0])
        pupil_point_refraction = np.array([1.31681088, 2.02435105, 49.13473422])
        cornea_center = np.array([1.46826769, 1.99285342, 48.37022867])
        R = 0.78
        n1 = 1.3375
        n2 = 1

        iota = calculate_iota(camera_position_wcs, pupil_point_refraction, cornea_center, R, n1, n2)

        expected_value = np.array([0.35314408, -0.03851277, -0.93477593])
        np.testing.assert_array_almost_equal(iota, expected_value)

    def test_calculate_p(self):

        pupil_point_refraction = np.array([1.31681088, 2.02435105, 49.13473422])
        cornea_center = np.array([1.46826769, 1.99285342, 48.37022867])
        R_const = 0.78
        K_const = 0.42
        iota_unit_vector= np.array([0.35314408, -0.03851277, -0.93477593])

        pupil_center = calculate_p(r=pupil_point_refraction, c=cornea_center, R=R_const, K=K_const, iota=iota_unit_vector)

        expected_value = np.array([1.18632962, 2.03858092, 49.48011944])
        np.testing.assert_array_almost_equal(pupil_center, expected_value)

    def test_calculate_optic_axis_unit_vector(self):

        camera_position_wcs = np.array([0, 0, 0])
        pupil_center_wcs = np.array([-0.03216, -0.04944, -1.2])
        cornea_center = np.array([1.46826769, 1.99285342, 48.37022867])
        R_const = 0.78
        K_const = 0.42
        n1_const = 1.3375
        n2_const = 1

        omega = \
            calculate_optic_axis_unit_vector(pupil_center_wcs, camera_position_wcs, cornea_center, R_const, K_const, n1_const, n2_const)

        expected_value = np.array([-0.24600787, 0.03989999, 0.96844624])
        np.testing.assert_array_almost_equal(omega, expected_value)



if __name__ == '__main__':
    unittest.main()