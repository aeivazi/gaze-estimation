from math import cos, sin, radians
import numpy as np


def calculate_rotation_matrix_extrinsic(alpha_degree, beta_degree, gamma_degree):
    """
    Applies extrinsic rotation defined by Euler angles alpha, beta, gamma.
    Counter-clockwise transformation for angles is used.

    Rotational matrix is a multiplication of the basic rotations over one axis.

    R = Rz(gamma)*Ry(beta)*Rx(alpha)

    where basic rotations are:

                 1    0        0
    Rx(alpha) =  0 cos(alpha) -sin(alpha)
                 0 sin(alpha)  cos(alpha)

                cos(beta)    0  sin(beta)
    Ry(beta) =     0         1     0
                -sin(beta)   0  cos(beta)

                cos(gamma) -sin(gamma)  0
    Rz(gamma) = sin(gamma)  cos(gamma)  0
                0              0        1

    The order of angles transformations is the very important,
    pay attention here we first transform gamma around z,
    then beta around y and then alpha around x.

    :param
    alpha: rotation around x axis (degrees)
    beta:  rotation around y axis (degrees)
    gamma: rotation around z axis (degrees)
    :return:
    3x3 rotational matrix
    """

    alpha_rad = radians(alpha_degree)
    beta_rad  = radians(beta_degree)
    gamma_rad = radians(gamma_degree)

    Rx = [[1,    0,             0    ],
          [0, cos(alpha_rad), -sin(alpha_rad)],
          [0, sin(alpha_rad),  cos(alpha_rad)]]

    Ry = [[cos(beta_rad),  0, sin(beta_rad) ],
          [    0,          1,      0        ],
          [-sin(beta_rad), 0, cos(beta_rad)]]

    Rz = [[cos(gamma_rad), -sin(gamma_rad), 0],
          [sin(gamma_rad),  cos(gamma_rad), 0],
          [    0,                  0,       1]]

    R = np.dot(np.dot(Rz, Ry), Rx)

    return R

