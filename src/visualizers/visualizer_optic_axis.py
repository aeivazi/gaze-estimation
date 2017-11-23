
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from src.calculate_cornea_center import calculate_q, calculate_c

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

    x, y, z = zip(*line_array)
    ax.plot(x, y, z, c=color)
    ax.scatter(*(line_array[1]), c=color, marker=marker, s=size)


def draw_u_c(u, light, color):

    kq = [57, 52, 52.1, 50, 47, 46., 30, 20]

    ax.scatter(*u, c=color, marker='*', s=50)

    for kq_i in kq:
        q = calculate_q(kq_i, o_wcs_dummy, u)
        c = calculate_c(q, light, o_wcs_dummy, R)

        ax.scatter(*q, c=color, marker='*', s=50)
        ax.scatter(*c, c=color, marker='o', s=50)
        draw_line(q, c, magnitude_maltiply=1, color=color, marker='o', size=50)




if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # ax.scatter(*o_wcs_dummy, c=camera_color, marker='*', s=50)
    # ax.scatter(*l1_wcs_dummy, c=left_light_color, marker='v', s=50)

    u1 = np.array([-0.03482400000000001, -0.063, -1.2])
    draw_u_c(u1, light = l1_wcs_dummy, color=left_glint_projection)

    u2 = np.array([-0.04365599999999999, -0.062784, -1.2])
    draw_u_c(u2, light = l2_wcs_dummy,  color=right_glint_projection)

    # ax.scatter(*q, c=left_glint_projection, marker='*', s=50)
    # ax.scatter(*c, c=left_glint_projection, marker='o', s=50)
    # draw_line(q, c, magnitude_maltiply=1, color=left_light_color, marker='o', size=50)


    -0.24600787, 0.03989999, 0.96844624

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    ax.view_init(elev=96, azim=90)

    plt.show()