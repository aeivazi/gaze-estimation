# All equations are taken from PhD thesis:
# Remote, Non-Contact Gaze Estimation with Minimal Subject Cooperation
# Guestrin, Elias Daniel
# https://tspace.library.utoronto.ca/handle/1807/24349

# @author: Anna Eivazi

from src.coordinate_system_transformations import transform_2D_to_3D
from src.calculate_cornea_center import calculate_cornea_center
from src.calculate_optic_axis import calculate_optic_axis_unit_vector
from src.calculate_visual_axis import calculate_visual_axis_unit_vector
from src.coordinate_system_transformations import transform_3D_to_3D


def transform_to_screen_coordinate_system(center_of_cornea_curvature, visual_axis_unit_vector, angles):
    center_of_cornea_curvature_scs = transform_3D_to_3D(center_of_cornea_curvature, *angles, 0, 0, 0)
    visual_axis_unit_vector_scs = transform_3D_to_3D(visual_axis_unit_vector, *angles, 0, 0, 0)

    return center_of_cornea_curvature_scs, visual_axis_unit_vector_scs


def calculate_point_of_interest(center_of_cornea_curvature, visual_axis_unit_vector, z_shift):
    """
    Calculates point of interest.
    Based on formula 2.31 and 3.61 calculations.

    :param center_of_cornea_curvature: center of cornea curvature
    :param optic_axis_unit_vector: unit vector of optic axis
    :param z_shift: z offset of the screen
    """

    # Formula 3.61
    kg = (z_shift - center_of_cornea_curvature[2]) / visual_axis_unit_vector[2]

    # Formula 2.31
    point_of_interest = center_of_cornea_curvature + kg * visual_axis_unit_vector

    return point_of_interest


def get_point_of_interest(glint_1_ics, glint_2_ics, pupil_center_ics, **kwargs):
    """
    End-to-end calculations.

    :param glint_1_ics: glint 1 coordinates in Image Coordinate System
    :param glint_2_ics: glint 2 coordinates in Image Coordinate System
    :param pupil_center_ics: glint 2 coordinates in Image Coordinate System
    :param kwargs: constants dictionary (check in integration_test.constants for an example)
    """

    cornea_center =  calculate_cornea_center(glint_1_ics, glint_2_ics, **kwargs)

    pupil_on_image_wgs = \
        transform_2D_to_3D(*pupil_center_ics, kwargs['focal_length_cm'], *kwargs['pixel_size_cm'], *kwargs['principal_point'])

    optic_axis_unit_vector = calculate_optic_axis_unit_vector(pupil_on_image_wgs,
                                                              kwargs['camera_position_wcs'],
                                                              cornea_center,
                                                              kwargs['R_cm'],
                                                              kwargs['K_cm'],
                                                              kwargs['n1'],
                                                              kwargs['n2'])

    visual_axis_unit_vector =\
        calculate_visual_axis_unit_vector(optic_axis_unit_vector,
                                          kwargs['alpha_right'],
                                          kwargs['beta'])

    point_of_interest = \
        calculate_point_of_interest(cornea_center,
                                    visual_axis_unit_vector,
                                    kwargs['z_shift'])

    return point_of_interest

