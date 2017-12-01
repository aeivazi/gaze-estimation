
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from src.coordinate_system_transformations import transform_2D_to_3D
from src.calculate_optic_axis import calculate_optic_axis_unit_vector
from src.calculate_cornea_center import calculate_cornea_center
from tests.point_of_interest_test import constants

left_light_color = 'blue'
right_light_color = 'red'
camera_color = 'yellow'
left_glint_projection = 'blue'
right_glint_projection = 'red'

o_wcs_dummy = [0, 0, 0]
l1_wcs_dummy = [-23, 0, 0]
l2_wcs_dummy = [23, 0, 0]
R = 0.9


def draw_line(point1, point2, magnitude_maltiply=1, color='b', marker='*', size=20):

    if magnitude_maltiply == 1:
        line_array = [point1, point2]
    else:
        unit_vector = (point2 - point1) / np.linalg.norm(point2 - point1)
        line_array = [point1, point1 + magnitude_maltiply* unit_vector]
        print(unit_vector)
        print(point1 + magnitude_maltiply* unit_vector)

    x, y, z = zip(*line_array)
    ax.plot(x, y, z, c=color)
    ax.scatter(*(line_array[1]), c=color, marker=marker, s=size)


def calculate_optic_axis(pupil_center_ics, cornea_center, **kwargs):

    pupil_on_image_wgs = \
        transform_2D_to_3D(*pupil_center_ics, kwargs['focal_length_cm'], *kwargs['pixel_size_cm'],
                           *kwargs['principal_point'])

    optic_axis_unit_vector = calculate_optic_axis_unit_vector(pupil_on_image_wgs,
                                                              kwargs['camera_position_wcs'],
                                                              cornea_center,
                                                              kwargs['R_cm'],
                                                              kwargs['K_cm'],
                                                              kwargs['n1'],
                                                              kwargs['n2'])

    return optic_axis_unit_vector




if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    glint_1_ics = (327.45, 168.75)
    glint_2_ics = (309.05, 169.2)
    pupil_center_ics = (322.9, 173.3)

    cornea_center = calculate_cornea_center(glint_1_ics, glint_2_ics, **constants)

    optic_axis_unit_vector = calculate_optic_axis(pupil_center_ics, cornea_center, **constants)

    print('Cornea center: {}'.format(cornea_center))
    print('Optic axis unit vector: {}'.format(optic_axis_unit_vector))

    ax.scatter(*constants['camera_position_wcs'], c=camera_color, marker='*', s=50)
    ax.scatter(*constants['light_1_wcs'], c=left_light_color, marker='v', s=50)

    # ax.scatter(*cornea_center, c=left_glint_projection, marker='o', s=50)
    #
    ax.scatter(*optic_axis_unit_vector, c=left_light_color, marker='*', s=50)
    # draw_line(constants['camera_position_wcs'], optic_axis_unit_vector, magnitude_maltiply=1, color=left_light_color, marker='o', size=50)
    draw_line(cornea_center, cornea_center+optic_axis_unit_vector, magnitude_maltiply=50, color=left_light_color,
              marker='*', size=50)

    # ax.scatter(*q, c=left_glint_projection, marker='*', s=50)

    # draw_line(q, c, magnitude_maltiply=1, color=left_light_color, marker='o', size=50)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    ax.view_init(elev=96, azim=90)

    plt.show()