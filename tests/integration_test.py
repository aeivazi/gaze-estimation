import unittest
import numpy as np
import math
from collections import OrderedDict

from src.calculate_point_of_interest import get_point_of_interest

# A note on coordinate systems.

# In our code we defined World Coordinate System (WCS) = Camera Coordinate System.
# WCS is a right-hand coordinate system, where axis defined as:
# X-axis is horizontal pointing left,
# Y-axis is vertical pointing up,
# Z-axis points towards the subject.
# Unit is centimeter.
#
#
# Screen coordinate system (SCS) has a zero in nodal point of camera, but aligned with vertical screen.
# If camera would be installed without angles, it would mean SCS = WSC = CCS.

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
    'camera_rotation': np.array([math.radians(8), 0, 0]) # rotation only over X axis
}


class TestIntegration(unittest.TestCase):

    def test_end_to_end_calculations(self):

        test_data = OrderedDict(
            {
                1: {
                    'glint1': (332, 164),
                    'glint2': (322, 169),
                    'glint3': (313, 165),
                    'pupil': (323, 163),
                    'point_on_screen': (490, 65)
                },
                2: {
                    'glint1': (333, 164),
                    'glint2': (323, 169),
                    'glint3': (314, 165),
                    'pupil': (324, 163),
                    'point_on_screen': (840, 65)
                },
                3: {
                    'glint1': (324.5, 164.4),
                    'glint2': (314.9, 168.4),
                    'glint3': (305.6, 164),
                    'pupil': (305.3, 159.5),
                    'point_on_screen': (1190, 65)
                },
                4: {
                    'glint1': (327.45, 168.75),
                    'glint2': (318.3, 172.4),
                    'glint3': (309.05, 169.2),
                    'pupil': (322.9, 173.3),
                    'point_on_screen': (490, 520)
                },
                5: {
                    'glint1': (322.711, 168.816),
                    'glint2': (313.447, 172.579),
                    'glint3': (304.579, 169.211),
                    'pupil': (310.421, 171.658),
                    'point_on_screen': (840, 520)
                },
                6: {
                    'glint1': (317.78, 168.707),
                    'glint2': (308.78, 172.561),
                    'glint3': (299.561, 169.122),
                    'pupil': (300.463, 173.024),
                    'point_on_screen': (1190, 520)
                },
                7: {
                    'glint1': (330.5, 175.5),
                    'glint2': (320.667, 179),
                    'glint3': (311, 176),
                    'pupil': (320, 185.5),
                    'point_on_screen': (490, 975)
                },
                8: {
                    'glint1': (321.722, 174.583),
                    'glint2': (312.75, 178.389),
                    'glint3': (303.389, 174.722),
                    'pupil': (310.278, 185.556),
                    'point_on_screen': (840, 975)
                },
                9: {
                    'glint1': (317.2, 174.933),
                    'glint2': (308.267, 178.567),
                    'glint3': (298.933, 174.933),
                    'pupil': (302.967, 186.1),
                    'point_on_screen': (1190, 975)
                }
            }
        )

        output = []
        for point_name, point in test_data.items():

            # if point_name not in [4, 5, 6]:
            #     continue

            point_of_interest = get_point_of_interest(point['glint1'], point['glint3'], point['pupil'], **constants)
            #np.testing.assert_array_almost_equal(point_of_interest, point['poi'])
            output.append(point_of_interest)



        print('{} {} {}'.format(output[0], output[1], output[2]))
        print('{} {} {}'.format(output[3], output[4], output[5]))
        print('{} {} {}'.format(output[6], output[7], output[8]))


if __name__ == '__main__':
    unittest.main()