
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from src.coordinate_system_transformations import transform_2D_to_3D
from src.calculate_optic_axis import calculate_optic_axis_unit_vector, calculate_r, calculate_p
from src.calculate_cornea_center import calculate_cornea_center

left_light_color = 'blue'
right_light_color = 'red'
camera_color = 'yellow'
left_glint_projection = 'blue'
right_glint_projection = 'red'


constants = {
    'light_1_wcs': np.array([-23, 0, 0]),
    'light_2_wcs': np.array([23, 0, 0]),
    'camera_position_wcs': np.array([0, 0, 0]),
    'focal_length_cm': 1.2,
    'pixel_size_cm': (0.00048, 0.00048),
    'principal_point': (400, 300),
    'z_shift': -18,
    'alpha_right': math.radians(-5),
    'beta': math.radians(1.5),
    'R_cm': 0.78,
    'K_cm': 0.42,
    'n1': 1.3375,
    'n2': 1,
    'distance_to_camera_cm': 52,
    'camera_angle': math.radians(8)
}


def draw_line(point1, point2, magnitude_maltiply=1, color='b', size=20):

    if magnitude_maltiply == 1:
        line_array = [point1, point2]
    else:
        unit_vector = (point2 - point1) / np.linalg.norm(point2 - point1)
        line_array = [point1, point1 + magnitude_maltiply* unit_vector]

    x, y, z = zip(*line_array)
    ax.plot(x, y, z, c=color)


def draw_unit_vector(unit_vector, starting_point=np.array([0, 0, 0]), magnitude_maltiply=1, color='b', size=20):

    line_array = [starting_point, starting_point + magnitude_maltiply * unit_vector]

    x, y, z = zip(*line_array)
    ax.plot(x, y, z, c=color)
    ax.scatter(*(line_array[1]), c=color, marker='*', s=size)




if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    glint_1_ics = (327.45, 168.75)
    glint_2_ics = (309.05, 169.2)
    pupil_center_ics = (322.9, 173.3)

    # Cornea center of curvature in WCS
    cornea_center_of_curvature_wcs = calculate_cornea_center(glint_1_ics, glint_2_ics, **constants)

    # Pupil center on image in WCS
    pupil_on_image_wcs = transform_2D_to_3D(*pupil_center_ics,
                                            constants['focal_length_cm'],
                                            *constants['pixel_size_cm'],
                                            *constants['principal_point'])

    # Optic axis unit vector (iota)
    optic_axis_unit_vector = calculate_optic_axis_unit_vector(pupil_on_image_wcs,
                                                              constants['camera_position_wcs'],
                                                              cornea_center_of_curvature_wcs,
                                                              constants['R_cm'],
                                                              constants['K_cm'],
                                                              constants['n1'],
                                                              constants['n2'])

    print('Pupil wcs {}'.format(pupil_on_image_wcs))
    print('Cornea center: {}'.format(cornea_center_of_curvature_wcs))
    print('Optic axis unit vector: {}'.format(optic_axis_unit_vector))

    ax.scatter(*constants['camera_position_wcs'], c=camera_color, marker='*', s=50)
    ax.scatter(*constants['light_1_wcs'], c=left_light_color, marker='v', s=50)

    ax.scatter(*cornea_center_of_curvature_wcs, c=left_glint_projection, marker='o', s=50)

    draw_unit_vector(optic_axis_unit_vector, starting_point=cornea_center_of_curvature_wcs, magnitude_maltiply=1, color='red')


    ### Intermidiate points and unit vectors

    # # Pupil point of refraction(r) in WCS
    pupil_point_of_refraction_wcs = calculate_r(constants['camera_position_wcs'],
                                                pupil_on_image_wcs,
                                                cornea_center_of_curvature_wcs,
                                                constants['R_cm'])

    pupil_center_wcs = \
        calculate_p(constants['camera_position_wcs'],
                    pupil_point_of_refraction_wcs,
                    cornea_center_of_curvature_wcs,
                    constants['R_cm'], constants['K_cm'], constants['n1'], constants['n2'])

    ax.scatter(*pupil_point_of_refraction_wcs, c='blue', marker='*', s=50)
    ax.scatter(*pupil_center_wcs, c='blue', marker='*', s=50)
    draw_line(constants['camera_position_wcs'], pupil_point_of_refraction_wcs)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    ax.view_init(elev=10, azim=12)

    plt.show()