import numpy as np
from src.variables import *
import scipy.optimize as opt
from src.vector_functions import normalize, calculate_magnitude

# i - is number of lights
# i = 1,2
#
# Unknown
# q1 = (q1_1, q1_2, q1_2)
# q2 = (q2_1, q2_2, q2_2)
# c = (c_1, c_2, c_3)
# Kq1
# Kq2
# Kcb
#
# Given
# o = (o_1, o_2, o_3)
# 11 = (11_1, 11_2, 11_3)
# 12 = (12_1, 12_2, 12_3)
# u1 = (u1_1, u1_2, u1_3)
# u2 = (u2_1, u2_2, u2_3)
# R


def calculate_b_norm(o, l1, l2, u1, u2):
    """
    Calculates unit vector in the direction of the line of intersection of the planes (l1, 0, u1) and (l2, o, u2).
    Note that functions expects u1, u2 to be in WCS already.

    Equations:
    bnorm = b / ||b||

    b = [(l1 - o) x (u1 - o)] x [(l2 - o) x (u2 - o)]

    :param o: camera center
    :param l1: light 1 positions
    :param l2: light_1 positions
    :param u1: glint 1 positions (WCS)
    :param u2: glint 2 positions (WCS)
    :return: unit vector in WCS
    """

    # normal to the plane l1, o, u1
    l1_o_u1 = np.cross((l1 - o), (u1 - o))

    # normal to the plane l2, o, u2
    l2_o_u2 = np.cross((l2 - o), (u2 - o))

    # normal of normals :)
    b = np.cross(l1_o_u1, l2_o_u2)

    return normalize(b)

# Theory ref:
# a dot b =  a1*b1 + a2*b2 + ... + an*bn
# ||a - b|| = sqrt((a1 - b1)^2 + ... + (an - bn)^2)


def equations_system(variables, *known):
    # We take the unknowns
    c_1, c_2, c_3, q1_1, q1_2, q1_3, q2_1, q2_2, q2_3, Kq1, Kq2, Kcb = variables

    # Known
    u1, u2, o, l1, l2, bnorm, R = known

    #print('Variables {}'.format(variables))
    #print('Known {}'.format(known))

    # Equation (1)
    #
    # qi = o + Kqi * (o - ui)
    # =>
    # q1_1 = o_1 + Kq1 * (o_1 - u1_1)
    # q1_2 = o_2 + Kq1 * (o_2 - u1_2)
    # q1_3 = o_3 + Kq1 * (o_3 - u1_3)
    # q2_1 = o_1 + Kq2 * (o_1 - u2_1)
    # q2_2 = o_2 + Kq2 * (o_2 - u2_2)
    # q2_3 = o_3 + Kq2 * (o_3 - u2_3)
    eq1 = o[0] + Kq1 * (o[0] - u1[0]) - q1_1
    eq2 = o[1] + Kq1 * (o[1] - u1[1]) - q1_2
    eq3 = o[2] + Kq1 * (o[2] - u1[2]) - q1_3
    eq4 = o[0] + Kq2 * (o[0] - u2[0]) - q2_1
    eq5 = o[1] + Kq2 * (o[1] - u2[1]) - q2_2
    eq6 = o[2] + Kq2 * (o[2] - u2[2]) - q2_3

    # Equation (2)
    #
    # ||q_i - c|| = R
    # =>
    # (q1_1 - c_1)^2 + (q1_2 - c_2)^2 + (q1_3 - c_3)^2 = R^2
    # (q2_1 - c_1)^2 + (q2_2 - c_2)^2 + (q2_3 - c_3)^2 = R^2
    eq7 = (q1_1 - c_1)**2 + (q1_2 - c_2)**2 + (q1_3 - c_3)**2 - R**2
    eq8 = (q2_1 - c_1)**2 + (q2_2 - c_2)**2 + (q2_3 - c_3)**2 - R**2

    # Equation (4)
    #
    # (li - qi)dot(qi - c)*||o - qi|| = (o - qi)dot(qi - c)*||li - qi||
    #
    # (l1 - q1)dot(q1 - c) = (l1_1 - q1_1)*(q1_1 - c_1) + (l1_2 - q1_2)*(q1_2 - c_2) + (l1_3 - q1_3)*(q1_3 - c_3)
    # ||o - q1|| = sqrt((o_1 - q1_1)^2 + (o_2 - q1_2)^2 + (o_3 - q1_3)^2
    # (o - qi)dot(qi - c) = (o_1 - q1_1)*(q1_1 - c_1) + (o_2 - q1_2)*(q1_2 - c_2) + (o_2 - q1_2)*(q1_2 - c_2)
    # ||l1 - q1|| = sqrt((l1_1 - q1_1)^2 + (l1_2 - q1_2)^2 + (l1_3 - q1_3)^2

    eq9 = \
        (
            ((l1[0] - q1_1) * (q1_1 - c_1) + (l1[1] - q1_2) * (q1_2 - c_2) + (l1[2] - q1_3) * (q1_3 - c_3)) *
            np.sqrt((o[0] - q1_1) ** 2 + (o[1] - q1_2) ** 2 + (o[2] - q1_3) ** 2)
         ) - \
        (
            ((o[0] - q1_1) * (q1_1 - c_1) + (o[1] - q1_2) * (q1_2 - c_2) + (o[2] - q1_2) * (q1_2 - c_2)) *
            np.sqrt((l1[0] - q1_1) ** 2 + (l1[1] - q1_2) ** 2 + (l1[2] - q1_3) ** 2)
        )

    eq10 = \
        (
            ((l2[0] - q2_1) * (q2_1 - c_1) + (l2[1] - q2_2) * (q2_2 - c_2) + (l2[2] - q2_3) * (q2_3 - c_3)) *
            np.sqrt((o[0] - q2_1) ** 2 + (o[1] - q2_2) ** 2 + (o[2] - q2_3) ** 2)
        ) - \
        (
            ((o[0] - q2_1) * (q2_1 - c_1) + (o[1] - q2_2) * (q2_2 - c_2) + (o[2] - q2_2) * (q2_2 - c_2)) *
            np.sqrt((l2[0] - q2_1) ** 2 + (l2[1] - q2_2) ** 2 + (l2[2] - q2_3) ** 2)
        )

    # Equation (16)
    #
    # c - o = Kcb * bnorm
    # =>
    # c_1 - o_1 = Kcb * bnorm_1
    # c_2 - o_2 = Kcb * bnorm_2
    # c_3 - o_3 = Kcb * bnorm_3

    eq11 = c_1 - o[0] - Kcb * bnorm[0]
    eq12 = c_2 - o[1] - Kcb * bnorm[1]
    eq13 = c_3 - o[2] - Kcb * bnorm[2]

    #print('Equations'.format([eq1, eq2, eq3, eq4, eq5, eq6, eq8, eq9, eq10, eq11, eq12, eq13]))

    return [eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq11, eq12, eq13]


def calculate_c_wcs(u1_wcs, u2_wcs, o_wcs, l1_wcs, l2_wcs, R):
    """
    c - nodal point of the eye (center of corneal curvature)
    :return:
    c in WCS
    """

    b_norm =  calculate_b_norm(o_wcs, l1_wcs, l2_wcs, u1_wcs, u2_wcs)

    print('B_norm is: {}'.format(b_norm))

    known_data = (u1_wcs, u2_wcs, o_wcs, l1_wcs, l2_wcs, b_norm, R)

    (c_1_0, c_2_0, c_3_0) = (3, -20, 55)
    (q1_1_0, q1_2_0, q1_3_0) = (3.5, -20, 54)
    (q2_1_0, q2_2_0, q2_3_0) = (2.5, -20, 54)
    Kq1_0 = 40
    Kq2_0 = 40
    Kcb_0 = 50

    initial_solution = np.array((c_1_0, c_2_0, c_3_0, q1_1_0, q1_2_0, q1_3_0, q2_1_0, q2_2_0, q2_3_0, Kq1_0, Kq2_0, Kcb_0))
    print(initial_solution)

    solution = opt.fsolve(equations_system, initial_solution, known_data)

    print(solution)
    c_wcs = solution[0:3]

    return c_wcs


if __name__ == '__main__':
    c_wcs = calculate_c_wcs(u1_wcs_dummy, u2_wcs_dummy, o_wcs_dummy, l1_wcs_dummy, l2_wcs_dummy, R_const)
    print(c_wcs)
