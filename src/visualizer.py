
from src.variables import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from src.calculate_c import calculate_b_norm
from src.vector_functions import normalize, calculate_magnitude

left_light_color = 'blue'
right_light_color = 'red'
camera_color = 'yellow'
left_glint_projection = 'blue'
right_glint_projection = 'red'


def draw_arrow(point, shift=(0, 0, 0), color='b', marker='*', size=20):

    line_array = [shift, shift + point]

    x, y, z = zip(*line_array)
    ax.plot(x, y, z, c=color)
    ax.scatter(*(line_array[1]), c='r', marker=marker, s=size)


def visualize_b_norm():

    l1_o = l1_wcs_dummy-o_wcs_dummy
    u1_o = u1_wcs_dummy-o_wcs_dummy
    l1_o_u1 = np.cross(l1_o, u1_o)

    draw_arrow(l1_o, shift=o_wcs_dummy, color=left_light_color, marker='+', size=100)
    draw_arrow(u1_o, shift=o_wcs_dummy, color=left_light_color, marker='+', size=100)
    draw_arrow(10*normalize(l1_o_u1), shift=o_wcs_dummy, color='black', marker='+', size=100)

    l2_o = l2_wcs_dummy - o_wcs_dummy
    u2_o = u2_wcs_dummy - o_wcs_dummy
    l2_o_u2 = np.cross(l2_o, u2_o)

    draw_arrow(l2_o, shift=o_wcs_dummy, color=right_light_color, marker='+', size=100)
    draw_arrow(u2_o, shift=o_wcs_dummy, color=right_light_color, marker='+', size=100)
    draw_arrow(10*normalize(l2_o_u2), shift=o_wcs_dummy, color='black', marker='+', size=100)

    b = np.cross(l2_o_u2, l1_o_u1)
    b_norm = normalize(b)
    draw_arrow(10*b_norm, shift=o_wcs_dummy, color='green', marker='+', size=100)

    return


def visualize_input_data():
    ax.scatter(*u1_wcs_dummy, c=left_glint_projection, marker='^', s=50)
    ax.scatter(*u2_wcs_dummy, c=right_glint_projection, marker='^', s=50)

    ax.scatter(*o_wcs_dummy, c=camera_color, marker='s', s=50)
    ax.scatter(*l1_wcs_dummy, c=left_light_color, marker='*', s=50)
    ax.scatter(*l2_wcs_dummy, c=right_light_color, marker='*', s=50)

    return


if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    visualize_input_data()
    visualize_b_norm()


    cornea_position = np.array([3, -20, 55])

    ax.scatter(*cornea_position, c='pink', marker='s', s=150)
    c_o = cornea_position - o_wcs_dummy
    draw_arrow(c_o, shift=o_wcs_dummy, color='pink', marker='+', size=100)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    ax.view_init(elev=96, azim=90)

    plt.show()