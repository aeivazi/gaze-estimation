# Coordinate systems transformations
#
# @author: Anna Eivazi

import numpy as np
from .rotation_matrix import calculate_rotation_matrix_extrinsic


def transform_2D_to_3D(x, y,
                       focal_length,
                       pixel_size_x, pixel_size_y,
                       principal_point_x, principal_point_y):
    """
    Transforms 2D point on image coordinate system (ICS) to 3D point in camera coordinate system (CCS).
    Camera coordinate system is in units of length (e.g. cm). Image coordinate system is in pixel coordinate system.

    Camera coordinate system has zero in center of the lens, x axis left, y - up, z from lens towards the object.
    Image coordinate system has zero in the left-up corner of the image, x - right, y - down.

    As the image is flipped, the center is located in down-right corner of the camera matrix, x - left, y - up.

    x_ccs = (x_ics - principal_point_x)*pixel_size_x
    y_ccs = (y_ics - principal_point_y)*pixel_size_y
    z_css = -focal_length

    :param
    x_ics, y_ics: 2D coordinate in ICS
    focal_length: focal length in units of length (e.g. cm)
    pixel_size_x: the sixe of one pixel in x dimention in the same units of length (e.g. cm)
    pixel_size_y: the sixe of one pixel in y dimention in the same units of length (e.g. cm)
    principal_point_x, principal_point_y: the location of the zero point of CCS on the ICS (usually it is center of the camera matrix)

    :return: x_ccs, y_ccs, z_ccs: 3D point in CCS
    """

    x_ccs = (x - principal_point_x) * pixel_size_x
    y_ccs = (y - principal_point_y) * pixel_size_y
    z_ccs = -focal_length

    return x_ccs, y_ccs, z_ccs

def transform_3D_to_3D(x, y, z,
                       alpha, beta, gamma,
                       x_shift, y_shift, z_shift):
    """
    Projects 3D point in the input right handed coordinate system (CS_in) to
    the 3D point in the output right handed coordinate system (CS_out).

    (x_out)     (x_in)   (x_shift)
    (y_out) = R (y_in) + (y_shift)
    (z_out)     (z_in)   (z_shift)

    R - is extrinsic rotational matrix defined by Euler angles alpha, beta, gamma
    (x_shift, y_shift, z_shift) defines the shift of CS_out's center relatively to CS_in's center.


    :param
    x, y, z: 3D point in CS_in
    gamma, beta, alpha: rotation angles of axis (degree)
    x_shift, y_shift, z_shift: zero shift of coordinate systems
    :return:
    x_out, y_out, x_out: 3D point in CS_out
    """

    R = calculate_rotation_matrix_extrinsic(alpha, beta, gamma)

    vector_out = np.dot(R, [[x], [y], [z]]) + [[x_shift], [y_shift], [z_shift]]

    x_out = vector_out[0, 0]
    y_out = vector_out[1, 0]
    z_out = vector_out[2, 0]

    return x_out, y_out, z_out

