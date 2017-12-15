import numpy as np

# conversion from eye-tracker coordinates to WCS
u1_ics = np.array([])
u2_ics = np.array([])
v_ics = np.array([])




#light 1 position
l1_wcs_dummy = np.array([10, -20, 0])
#light 1 position
l2_wcs_dummy = np.array([-10, -20, 0])

focal_length = 1.2

#nodal point of the camera position
o_wcs_dummy = np.array([0, 0, 10])

#glint center location of the left eye
u1_wcs_dummy = np.array([-0.1, 0.6, o_wcs_dummy[2] - focal_length])
#glint center location of the right eye
u2_wcs_dummy = np.array([-0.15, 0.9, o_wcs_dummy[2] - focal_length])

#pupil location
v_wcs_dummy = np.array([1, -2, o_wcs_dummy[2] - focal_length])

# eye parameters
# these are typical parameters
# individual should be found via calibration

# radius of corneal curvature
# (cm)
R_const = 7.8 / 10

# distance between the center of the pupil and the center of corneal curvature
# (cm)
K_const = 4.2 / 10

# effective index of refraction of the cornea and the aqueous humor combined
# a.k.a. Standard Keratometric Index
# (dimensionless)
n1_const = 1.3375

# Horizontal angle between visual and optic axes of the eye
# (degree)
alpha_eye_right_const = -5
alpha_eye_left_const = 5

# Vertical angle between visual and optic axes of the eye
# (degree)
beta_eye_const = 1.5

# Distance between the center of corneal curvature and the center of rotation fo the eye
# (cm)
D_const = 5.3  / 10