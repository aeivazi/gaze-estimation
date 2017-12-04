# All equations are taken from PhD thesis:
# Remote, Non-Contact Gaze Estimation with Minimal Subject Cooperation
# Guestrin, Elias Daniel
# https://tspace.library.utoronto.ca/handle/1807/24349

# @author: Anna Eivazi

import numpy as np


def calculate_eye_angles(optic_axis_unit_vector):
    """
    Calculations based on A.19, A.20.

    Kappa is for now assumed to be zero.

    :param optic_axis_unit_vector: unit vector for optic axis
    :return: thera, phi, kappa in radians
    """

    theta = -1 * np.arctan(optic_axis_unit_vector[0]/optic_axis_unit_vector[2])
    phi = np.arcsin(optic_axis_unit_vector[1])
    kappa = 0

    return theta, phi, kappa


def calculate_rotation_matrix(theta, phi, kappa):
    """
    Calculations based on A.6 and A.2-A.5


    :param theta, phi, kappa angles in radians
    :return: 3x3 rotation matrix
    """

    R_flip = \
        np.array([[-1, 0, 0],
                  [ 0, 1, 0],
                  [ 0, 0, -1]])

    R_theta = \
        np.array([[ np.cos(theta), 0, -np.sin(theta)],
                  [      0,        1,    0          ],
                  [ np.sin(theta), 0, np.cos(theta)]])

    R_phi = \
        np.array([[ 1,      0,           0      ],
                  [ 0,  np.cos(phi), np.sin(phi)],
                  [ 0, -np.sin(phi), np.cos(phi)]])

    R_kappa = \
        np.array([[np.cos(kappa), -np.sin(kappa), 0],
                  [np.sin(kappa),  np.cos(kappa), 0],
                  [     0,             0,         1]])

    # R_eye = R_flip * R_theta * R_phi * R_kappa
    flip_theta = np.dot(R_flip, R_theta)
    flip_theta_phi = np.dot(flip_theta, R_phi)
    R_eye = np.dot(flip_theta_phi, R_kappa)

    return R_eye


def calculate_nu_ecs(alpha, beta):
    """

    Based on Formula 2.1

    :param alpha (radians): horizontal angle of visial axis compare to optical
    :param beta (radians): vertical angle of visial axis compare to optical
    :return: 3x1 rotation matrix
    """

    nu_ecs = \
        np.array([-np.sin(alpha)*np.cos(beta),
                   np.sin(beta),
                   np.cos(alpha)*np.cos(beta)])

    return nu_ecs


def calculate_visual_axis_unit_vector(optic_axis_unit_vector, alpha, beta):
    """

    Based on formula 2.30 calulations.

    :param optic_axis_unit_vector: unit vector of optic axis
    :param z_shift: z offset of the screen
    :param alpha: horizontal angle of visial axis compare to optical
    :param beta: vertical angle of visial axis compare to optical
    :return: coordinates of point of interest
    """
    nu_ecs = calculate_nu_ecs(alpha, beta)

    theta, phi, kappa = calculate_eye_angles(optic_axis_unit_vector)
    Reye = calculate_rotation_matrix(theta, phi, kappa)

    visual_axis_unit_vector = np.dot(Reye, nu_ecs)

    return visual_axis_unit_vector


def calculate_point_of_interest(c, optic_axis_unit_vector, z_shift, alpha, beta):
    """

    Based on formula 2.31 calulations.


    :param c: center of cornea curvature
    :param optic_axis_unit_vector: unit vector of optic axis
    :param z_shift: z offset of the screen
    :param alpha: horizontal angle of visial axis compare to optical
    :param beta: vertical angle of visial axis compare to optical
    """

    visual_axis_unit_vector = calculate_visual_axis_unit_vector(optic_axis_unit_vector, alpha, beta)

    # Formula 3.61
    kg = (z_shift - c[2]) / visual_axis_unit_vector[2]

    # Formula 2.31
    point_of_interest = c + kg * visual_axis_unit_vector

    return point_of_interest

