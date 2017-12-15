# All equations are taken from PhD thesis:
# Remote, Non-Contact Gaze Estimation with Minimal Subject Cooperation
# Guestrin, Elias Daniel
# https://tspace.library.utoronto.ca/handle/1807/24349

# @author: Anna Eivazi

import numpy as np
import scipy.optimize as opt

from src.coordinate_system_transformations import transform_2D_to_3D


def normalized(vector):
    """
    Returns normalized vector.
    """
    return vector/np.linalg.norm(vector)


def calculate_q(kq, o, u):
    """
    Calculates point of reflection using formula 3.2.
    Given parameters are assumed to be given in world coordinate system (WCS),
    thus calculated point is also returned in WCS.

    :param kq: unitless coefficient representing distance between q and o.
    :param o: nodal point of camera
    :param u: image of corneal reflection center
    :return: point of reflection
    """

    return o + kq * normalized(o - u)


def calculate_c(q, l, o, R):
    """
    Calculates cornea center coordinates based on formula 3.7
    All parameters are assumed to be given in world coordinate system.

    :param q: point of reflection
    :param l: light coordinates
    :param o: nodal point of camera
    :param R: radius of cornea surface
    :return: cornea center coordinates
    """
    l_q_unit = normalized(l - q)
    o_q_unit = normalized(o - q)
    c = q - R * normalized(l_q_unit + o_q_unit)
    return c


def distance_between_corneas(variables, *known):
    """
    Calculates distance between two cornea centers.
    The calculations are based on formulars 3.11, 3.7

    :param variables: kq1, kq2
    :param known: u1, u2, o, l1, l2, R
    :return: distance between two cornea centers.
    """

    kq1, kq2 = variables
    u1, u2, o, l1, l2, R = known

    q1 = calculate_q(kq1, o, u1)
    q2 = calculate_q(kq2, o, u2)

    cornea_center1 = calculate_c(q1, l1, o, R)
    cornea_center2 = calculate_c(q2, l2, o, R)

    distance_between_corneas = np.linalg.norm(cornea_center1 - cornea_center2)

    # print('kq1 {}, kq2 {}'.format(kq1, kq2))
    # print('q1 {}, q2 {}'.format(q1, q2))
    # print('distance_between_corneas {}'.format(distance_between_corneas))

    return distance_between_corneas


def calculate_cornea_center_wcs(u1_wcs, u2_wcs, o_wcs, l1_wcs, l2_wcs, R, initial_solution):
    """
    Estimates cornea center using equation 3.11:
    min ||c1(kq1) - c2(kq2)||

    The cornea center should have the same coordinates, however, in the presents of the noise it is not always the case.
    Thus, the task is to find such parameters kq1 and kq2 that will minimize the difference between corneas centers.
    During the calculations all parameters are assumed to be given in the units of World Coordinate System.

    :param u1_wcs: image of corneal reflection center from the light on the left
    :param u2_wcs: image of corneal reflection center from the light on the right
    :param o_wcs: nodal point of camera
    :param l1_wcs: light coordinates on the left
    :param l2_wcs: light coordinates on the right
    :param R: radius of cornea surface
    :return: cornea center
    """

    known_data = (u1_wcs, u2_wcs, o_wcs, l1_wcs, l2_wcs, R)
    sol = opt.minimize(distance_between_corneas, initial_solution, known_data)

    kq1, kq2 = sol.x

    q1 = calculate_q(kq1, o_wcs, u1_wcs)
    c1 = calculate_c(q1, l1_wcs, o_wcs, R)

    q2 = calculate_q(kq2, o_wcs, u2_wcs)
    c2 = calculate_c(q2, l2_wcs, o_wcs, R)

    return (c1 + c2)/2


def calculate_cornea_center(u1_ics, u2_ics, **kwargs):

    u1_wcs = transform_2D_to_3D(*u1_ics, kwargs['focal_length_cm'], *kwargs['pixel_size_cm'], *kwargs['principal_point'])
    u2_wcs = transform_2D_to_3D(*u2_ics, kwargs['focal_length_cm'], *kwargs['pixel_size_cm'], *kwargs['principal_point'])

    Kq1_init = kwargs['distance_to_camera_cm']
    Kq2_init = kwargs['distance_to_camera_cm']

    return calculate_cornea_center_wcs(u1_wcs,
                                       u2_wcs,
                                       kwargs['camera_position_wcs'],
                                       kwargs['light_1_wcs'],
                                       kwargs['light_2_wcs'],
                                       kwargs['R_cm'],
                                       (Kq1_init, Kq2_init))

