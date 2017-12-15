import unittest
import numpy as np
import math
from src.calculate_visual_axis import calculate_eye_angles, calculate_visual_axis_unit_vector, calculate_nu_ecs, calculate_rotation_matrix


class TestCalculateOpticAxis(unittest.TestCase):

    def test_calculate_eye_angles(self):

        omega = np.array([-0.210779, -0.221661, -0.952071])

        angles = calculate_eye_angles(omega)

        expected_value = np.array([-0.217876, -0.223518,  0])
        np.testing.assert_array_almost_equal(angles, expected_value)

    def test_calculate_nu_ecs(self):

        alpha = math.radians(0)
        beta = math.radians(0)
        nu_unit_vector = calculate_nu_ecs(alpha, beta)
        #no shift happens, unit vector should have a +z direction
        np.testing.assert_array_almost_equal(nu_unit_vector, np.array([0., 0., 1]))

        alpha = math.radians(45)
        beta = math.radians(0)
        nu_unit_vector = calculate_nu_ecs(alpha, beta)
        # no shift on Y and equal shift on Z and X
        np.testing.assert_array_almost_equal(nu_unit_vector, np.array([-0.707107, 0., 0.707107]))

        alpha = math.radians(90)
        beta = math.radians(0)
        nu_unit_vector = calculate_nu_ecs(alpha, beta)
        # no shift on Z and X
        np.testing.assert_array_almost_equal(nu_unit_vector, np.array([-1., 0., 0.]))

        alpha = math.radians(0)
        beta = math.radians(45)
        nu_unit_vector = calculate_nu_ecs(alpha, beta)
        # no shift on X and equal shift on Z and Y
        np.testing.assert_array_almost_equal(nu_unit_vector, np.array([0., 0.707107, 0.707107]))

        alpha = math.radians(45)
        beta = math.radians(45)
        nu_unit_vector = calculate_nu_ecs(alpha, beta)
        np.testing.assert_array_almost_equal(nu_unit_vector, np.array([-0.5, 0.707107, 0.5]))

        # common values for angles in eye tracking
        alpha = math.radians(-5)
        beta = math.radians(1.5)
        nu_unit_vector = calculate_nu_ecs(alpha, beta)
        np.testing.assert_array_almost_equal(nu_unit_vector, np.array([0.087126,  0.026177,  0.995853]))

    def test_calculate_rotation_matrix(self):
        theta = math.radians(0)
        phi = math.radians(0)
        kappa = math.radians(0)
        rotation_matrix = calculate_rotation_matrix(theta, phi, kappa)
        expected_value = np.array([[-1., 0., 0.],
                                   [ 0., 1., 0.],
                                   [ 0., 0., -1.]])
        np.testing.assert_array_almost_equal(rotation_matrix, expected_value)

        theta = math.radians(45)
        phi = math.radians(0)
        kappa = math.radians(0)
        rotation_matrix = calculate_rotation_matrix(theta, phi, kappa)
        expected_value = np.array([[-0.707107, 0., 0.707107],
                                   [0., 1., 0.],
                                   [-0.707107, 0., -0.707107]])
        np.testing.assert_array_almost_equal(rotation_matrix, expected_value)

        theta = math.radians(0)
        phi = math.radians(45)
        kappa = math.radians(0)
        rotation_matrix = calculate_rotation_matrix(theta, phi, kappa)
        expected_value = np.array([[-1., 0., 0.],
                                   [0., 0.707107, 0.707107],
                                   [0., 0.707107, -0.707107]])
        np.testing.assert_array_almost_equal(rotation_matrix, expected_value)

        theta = math.radians(0)
        phi = math.radians(0)
        kappa = math.radians(45)
        rotation_matrix = calculate_rotation_matrix(theta, phi, kappa)
        expected_value = np.array([[-0.707107, 0.707107, 0.],
                                   [ 0.707107, 0.707107, 0.],
                                   [0., 0., -1]])
        np.testing.assert_array_almost_equal(rotation_matrix, expected_value)

        theta = math.radians(45)
        phi = math.radians(45)
        kappa = math.radians(45)
        rotation_matrix = calculate_rotation_matrix(theta, phi, kappa)
        expected_value = np.array([[-0.853553,  0.146447,  0.5     ],
                                   [ 0.5     ,  0.5     ,  0.707107],
                                   [-0.146447,  0.853553, -0.5     ]])
        np.testing.assert_array_almost_equal(rotation_matrix, expected_value)


    def test_calculate_visual_axis(self):

        optic_axis_unit_vector = np.array([-0.210779, -0.221661, -0.952071])

        alpha_right = math.radians(-5)
        beta = math.radians(1.5)

        visual_axis_unit_vector = calculate_visual_axis_unit_vector(optic_axis_unit_vector, alpha_right, beta)

        expected_value = np.array([-0.296225, -0.195216, -0.934955])
        np.testing.assert_array_almost_equal(visual_axis_unit_vector, expected_value)

        self.assertAlmostEqual(np.linalg.norm(visual_axis_unit_vector), 1)


if __name__ == '__main__':
    unittest.main()