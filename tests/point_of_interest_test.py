import unittest
import numpy as np
import math
from src.point_of_interest import get_point_of_interest

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


class TestCalculateOpticAxis(unittest.TestCase):

    def test_calculate_point_of_interest(self):

        # test_data = {
        #     'point1': {
        #         'glint1': (341, 202), 'glint2': (326, 202), 'pupil': (340, 193), 'poi': np.array([-6.957012, 1.136131, -20])
        #     },
        #     'point2': {
        #         'glint1': (324, 204), 'glint2': (307, 205), 'pupil': (314, 198), 'poi': np.array([-6.80771503, 1.06634612, -20])
        #     },
        #     'point3': {
        #         'glint1': (334, 206), 'glint2': (315, 205), 'pupil': (314, 198), 'poi': np.array([-6.48752706, 0.99858833, -20])
        #     },
        #     'point4': {
        #         'glint1': (349, 199), 'glint2': (330, 199), 'pupil': (344, 195), 'poi': np.array([-6.35586757,  0.94984947, -20])
        #     },
        #     'point5': {
        #         'glint1': (333, 197), 'glint2': (315, 197), 'pupil': (322, 192), 'poi': np.array([-6.61017857,  0.96908146, -20])
        #     },
        #     'point6': {
        #         'glint1': (314, 215), 'glint2': (297, 215), 'pupil': (298, 210), 'poi': np.array([-6.899897, 1.153309, -20])
        #     },
        #     'point7': {
        #         'glint1': (328, 210), 'glint2': (311, 210), 'pupil': (325, 207), 'poi': np.array([-6.774135,  1.114313, -20])
        #     },
        #     'point8': {
        #         'glint1': (327, 204), 'glint2': (319, 204), 'pupil': (312, 204), 'poi': np.array([-8.867415, 1.700117, -20])
        #     },
        #     'point9': {
        #         'glint1': (327, 210), 'glint2': (310, 210), 'pupil': (310, 208), 'poi': np.array([-6.79179779, 1.11496562, -20])
        #     }
        # }

        test_data = {
            'point1': {
                'glint1': (332, 164),
                'glint2': (322, 169),
                'glint3': (313, 165),
                'pupil': (323, 163),
                'point_on_screen': (490, 65),
                'poi': np.array([-21.441883, 21.654643, -18])
            },
            'point2': {
                'glint1': (333, 164),
                'glint2': (323, 169),
                'glint3': (314, 165),
                'pupil': (324, 163),
                'point_on_screen': (840, 65),
                'poi': np.array([-21.441883, 21.654643, -18])
            },
            'point3': {
                'glint1': (324.5, 164.4),
                'glint2': (314.9, 168.4),
                'glint3': (305.6, 164),
                'pupil': (305.3, 159.5),
                'point_on_screen': (1190, 65),
                'poi': np.array([-21.441883, 21.654643, -18])
            },
            'point4': {
                'glint1': (327.45, 168.75),
                'glint2': (318.3, 172.4),
                'glint3': (309.05, 169.2),
                'pupil': (322.9, 173.3),
                'point_on_screen': (490, 520),
                'poi': np.array([-21.441883, 21.654643, -18])
            },
            'point5': {
                'glint1': (322.711, 168.816),
                'glint2': (313.447, 172.579),
                'glint3': (304.579, 169.211),
                'pupil': (310.421, 171.658),
                'point_on_screen': (840, 520),
                'poi': np.array([-21.441883, 21.654643, -18])
            },
            'point6': {
                'glint1': (317.78, 168.707),
                'glint2': (308.78, 172.561),
                'glint3': (299.561, 169.122),
                'pupil': (300.463, 173.024),
                'point_on_screen': (1190, 520),
                'poi': np.array([-21.441883, 21.654643, -18])
            },
            'point7': {
                'glint1': (330.5, 175.5),
                'glint2': (320.667, 179),
                'glint3': (311, 176),
                'pupil': (320, 185.5),
                'point_on_screen': (490, 975),
                'poi': np.array([-21.441883, 21.654643, -18])
            },
            'point8': {
                'glint1': (321.722, 174.583),
                'glint2': (312.75, 178.389),
                'glint3': (303.389, 174.722),
                'pupil': (310.278, 185.556),
                'point_on_screen': (840, 975),
                'poi': np.array([-21.441883, 21.654643, -18])
            },
            'point9': {
                'glint1': (317.2, 174.933),
                'glint2': (308.267, 178.567),
                'glint3': (298.933, 174.933),
                'pupil': (302.967, 186.1),
                'point_on_screen': (1190, 975),
                'poi': np.array([-21.441883, 21.654643, -18])
            }
        }

        # for point_name, point in test_data.items():
        #     point_of_interest = get_point_of_interest(point['glint1'], point['glint3'], point['pupil'], **constants)
        #     #np.testing.assert_array_almost_equal(point_of_interest, point['poi'])
        #
        #     print(point_name)
        #     print(point['point_on_screen'])
        #     print(point_of_interest)
        #     print('==============================')

        # point = test_data['point1']
        # point_of_interest = get_point_of_interest(point['glint1'], point['glint3'], point['pupil'], **constants)
        # print('point1')
        # print(point['point_on_screen'])
        # print(point_of_interest)
        # print('==============================')
        #
        # point = test_data['point2']
        # point_of_interest = get_point_of_interest(point['glint1'], point['glint3'], point['pupil'], **constants)
        # print('point2')
        # print(point['point_on_screen'])
        # print(point_of_interest)
        # print('==============================')
        #
        # point = test_data['point3']
        # point_of_interest = get_point_of_interest(point['glint1'], point['glint3'], point['pupil'], **constants)
        # print('point3')
        # print(point['point_on_screen'])
        # print(point_of_interest)
        # print('==============================')

        point = test_data['point4']
        point_of_interest = get_point_of_interest(point['glint1'], point['glint3'], point['pupil'], **constants)
        print('point4')
        print(point['point_on_screen'])
        print(point_of_interest)
        print('==============================')

        point = test_data['point5']
        point_of_interest = get_point_of_interest(point['glint1'], point['glint3'], point['pupil'], **constants)
        print('point5')
        print(point['point_on_screen'])
        print(point_of_interest)
        print('==============================')

        point = test_data['point6']
        point_of_interest = get_point_of_interest(point['glint1'], point['glint3'], point['pupil'], **constants)
        print('point6')
        print(point['point_on_screen'])
        print(point_of_interest)
        print('==============================')

        # point = test_data['point7']
        # point_of_interest = get_point_of_interest(point['glint1'], point['glint3'], point['pupil'], **constants)
        # print('point7')
        # print(point['point_on_screen'])
        # print(point_of_interest)
        # print('==============================')
        #
        # point = test_data['point8']
        # point_of_interest = get_point_of_interest(point['glint1'], point['glint3'], point['pupil'], **constants)
        # print('point8')
        # print(point['point_on_screen'])
        # print(point_of_interest)
        # print('==============================')
        #
        # point = test_data['point9']
        # point_of_interest = get_point_of_interest(point['glint1'], point['glint3'], point['pupil'], **constants)
        # print('point9')
        # print(point['point_on_screen'])
        # print(point_of_interest)
        # print('==============================')




if __name__ == '__main__':
    unittest.main()