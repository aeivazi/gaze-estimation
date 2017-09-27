
def project_2D_to_3D(x, y,
                     focal_length,
                     pixel_size_x, pixel_size_y,
                     principal_point_x, principal_point_y,
                     camera_monitor_distance):
    """
    Projects 2D point on image coordinate system (ICS) to 3D point on camera coordinate system (CCS).

    We assume, that pixels are rectangular, so no skewing is taken into account.
    We also assume that distance between image plane and camera center is focal_length.

    Transformation matrix between ics and ccs is:

    (x_ics)   | fx  0 cx | (x_ccs)
    (y_ics) = | 0 fy  cy | (y_ccs)
    (  1  )   | 0  0  1  | (z_ccs)

    where
    fx = focal_length/pixel_size_x
    fy = focal_length/pixel_size_y
    cx = principal_point_x
    cy = principal_point_y

    This gives us following equations:

    x_css = (x_ics - cx)*z_ccs/fx
    y_css = (y_ics - cy)*z_ccs/fy
    z_css = camera_monitor_distance

    :param
    x_ics, y_ics: 2D coordinate in ICS
    focal_length: focal length in units of length (e.g. cm)
    pixel_size_x: the sixe of one pixel in x dimention in the same units of length (e.g. cm)
    pixel_size_y: the sixe of one pixel in y dimention in the same units of length (e.g. cm)
    principal_point_x, principal_point_y: the location of the zero point of CCS on the ICS (usually it is center of the camera matrix)
    camera_monitor_distance: distance to monitor from camera in the same units of length (e.g. cm)
    :return: x_ccs, y_ccs, z_ccs: 3D point in CCS
    """

    x_ccs = (x - principal_point_x) * camera_monitor_distance * pixel_size_x / focal_length
    y_ccs = (y - principal_point_y) * camera_monitor_distance * pixel_size_y / focal_length
    z_ccs = camera_monitor_distance

    return x_ccs, y_ccs, z_ccs


def project_3D_to_2D(x, y, z,
                     focal_length,
                     pixel_size_x, pixel_size_y,
                     principal_point_x, principal_point_y):
    """
    Projects 3D point on camera coordinate system (CCS) to 2D point on image coordinate system (ICS).

    We assume, that pixels are rectangular, so no skewing is taken into account.
    We also assume that distance between image plane and camera center is focal_length.

    Transformation matrix between ics and ccs is:

    (x_ics)   | fx  0 cx | (x_ccs)
    (y_ics) = | 0 fy  cy | (y_ccs)
    (  1  )   | 0  0  1  | (z_ccs)

    where
    fx = focal_length/pixel_size_x
    fy = focal_length/pixel_size_y
    cx = principal_point_x
    cy = principal_point_y

    This gives us following equations:

    x_ics = fx*x_ccs/z_ccs + cx
    y_ics = fy*y_ccs/z_ccs + cy

    :param
    x_ccs, y_ccs, z_ccs: 3D point in CCS
    focal_length: focal length in units of length (e.g. cm)
    pixel_size_x: the sixe of one pixel in x dimention in the same units of length (e.g. cm)
    pixel_size_y: the sixe of one pixel in y dimention in the same units of length (e.g. cm)
    principal_point_x, principal_point_y: the location of the zero point of CCS on the ICS (usually it is center of the camera matrix)
    :return: x_ics, y_ics: 2D coordinate in ICS
    """

    x_ics = x * focal_length / (pixel_size_x * z) + principal_point_x
    y_ics = y * focal_length / (pixel_size_y * z) + principal_point_y

    return x_ics, y_ics