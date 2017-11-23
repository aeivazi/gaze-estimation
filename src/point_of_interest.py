# All equations are taken from PhD thesis:
# Remote, Non-Contact Gaze Estimation with Minimal Subject Cooperation
# Guestrin, Elias Daniel
# https://tspace.library.utoronto.ca/handle/1807/24349

# @author: Anna Eivazi

from src.coordinate_system_transformations import transform_2D_to_3D
from src.calculate_cornea_center import calculate_cornea_center
from src.calculate_optic_axis import calculate_optic_axis_unit_vector
from src.calculate_visual_axis import calculate_point_of_interest, calculate_visual_axis_unit_vector


def get_point_of_interest(glint_1_ics, glint_2_ics, pupil_center_ics, **kwargs):

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

    visual_axis_unit_vector = \
        calculate_visual_axis_unit_vector(optic_axis_unit_vector,
                                          kwargs['alpha_right'],
                                          kwargs['beta'])

    point_of_interest = \
        calculate_point_of_interest(cornea_center,
                                    visual_axis_unit_vector,
                                    kwargs['z_shift'])

    print('cornea_center: {}'.format(cornea_center))
    print('optic_axis_unit_vector: {}'.format(optic_axis_unit_vector))
    print('visual_axis_unit_vector: {}'.format(visual_axis_unit_vector))


    return point_of_interest

