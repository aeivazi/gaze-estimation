# All equations are taken from PhD thesis:
# Remote, Non-Contact Gaze Estimation with Minimal Subject Cooperation
# Guestrin, Elias Daniel
# https://tspace.library.utoronto.ca/handle/1807/24349

# @author: Anna Eivazi

from src.variables import *
import math


def squared_magnitude(vector):
    magnitude = np.linalg.norm(vector)
    return magnitude**2


def calculate_kr(o, v, c, R):
    """
    Calculates Kr based on Formula 3.29

    (o-v)**2 * kr**2 + 2*(o - v)(o -c )*kr + (o -c)**2 - R**2 = 0
    Which is a quadratic equation in the form of:
    a*kr**2 + 2b*kr + c = 0
    thus formula for kr is:

    kr = (-b + sqrt(b**2 - a*c))/a

    Take into account that for vector v:
    v dot v = norm(v)**2


    :param o: camera nodal point
    :param v: pupil center on image
    :param c: center of cornea curvature
    :param R: radius of cornea curvature
    :return: kr
    """

    a = squared_magnitude(o - v)
    b = np.dot(o - v, o -c )
    c = squared_magnitude(o - c) - R**2

    kr = (-b + math.sqrt(b**2 - a*c))/a

    return kr


def calculate_r(kr, o, v):
    """
    Calculates point of refraction of pupil center based on Formula 2.42

    :param kr: unitless coefficient kr
    :param o: camera nodal point
    :param v: pupil center on image
    :return: Coordinates of point of refraction of pupil center
    """

    r = o + kr * (o - v)
    return r


def calculate_iota(o, r, c, R, n1, n2):
    """
    Calculates a unit vector in the direction of the incident ray originating at the pupil center.

    Used Formulas: 3.31-3.33

    :param o: camera nodal point
    :param r: pupil point of reflection
    :param c: center of cornea curvature
    :param R: radius of cornea curvature
    :param n1: effective index of refraction of the aqueous humor and cornea combined (= 1.3375)
    :param n2: the index of refraction of air ( ≅ 1).
    :return: unit vector in the direction of the incident ray originating at the pupil center
    """

    # Formula 3.31
    zeta = (o - r)/np.linalg.norm(o - r)

    # Formula 3.32
    eta = (r - c)/R

    # Formula 3.33
    eta_dot_zeta = np.dot(eta, zeta)
    a = eta_dot_zeta - math.sqrt((n1/n2)**2 - 1 + eta_dot_zeta**2)
    iota = (n2/n1)*(a*eta - zeta)

    return iota


def calculate_p(r, c, R, K, iota):
    """
    Calculates pupil center coordinates.

    Used Formulas: 3.37, 3.34

    :param o: camera nodal point
    :param r: pupil point of reflection
    :param c: center of cornea curvature
    :param R: radius of cornea curvature
    :param K: distance between the center of the pupil and the center of corneal curvature
    :param iota: unit vector in the direction of the incident ray originating at the pupil center
    :return: pupil center
    """

    # Formula 3.37
    r_cxiota = np.dot((r-c), iota)
    kp = -1*r_cxiota - math.sqrt(r_cxiota**2 - (R**2 - K**2))

    # Formula 3.34
    p = r - kp*iota
    return p


def calculate_optic_axis_unit_vector(pupil_wcs, camera_wcs, cornea_wcs, R, K, n1, n2):
    """

    Calculates unit vector in the direction of the optic axis.

    :param pupil_wcs: pupil point of reflection
    :param camera_wcs: camera nodal point
    :param cornea_wcs: center of cornea curvature
    :param R: radius of cornea curvature
    :param K: distance between the center of the pupil and the center of corneal curvature
    :param n1: effective index of refraction of the aqueous humor and cornea combined (= 1.3375)
    :param n2: the index of refraction of air ( ≅ 1).
    :return: unit vector in the direction of the optic axis
    """

    kr = calculate_kr(camera_wcs, pupil_wcs, cornea_wcs, R)

    r = calculate_r(kr, camera_wcs, pupil_wcs)

    iota = calculate_iota(camera_wcs, r, cornea_wcs, R, n1, n2)

    p = calculate_p(r, cornea_wcs, R, K, iota)

    #Formula 3.38
    omega = (p - cornea_wcs)/np.linalg.norm(p - cornea_wcs)

    return omega

