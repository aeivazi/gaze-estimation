# All equations are taken from PhD thesis:
# Remote, Non-Contact Gaze Estimation with Minimal Subject Cooperation
# Guestrin, Elias Daniel
# https://tspace.library.utoronto.ca/handle/1807/24349

# @author: Anna Eivazi

from src.variables import *
import scipy.optimize as opt


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
    :param o: nodal point of camera
    :return: cornea center coordinates
    """
    l_q_unit = normalized(l - q)
    o_q_unit = normalized(o - q)
    return q - R * (l_q_unit + o_q_unit)/np.linalg.norm(l_q_unit + o_q_unit)


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

    q1 = calculate_q(sol.x[0], o_wcs, u1_wcs)
    cornea_center = calculate_c(q1, l1_wcs, o_wcs, R)

    return cornea_center

