import numpy as np

def deg_2_rad(deg, bounded=True):
    """ Returns radian value from deg. Bounded=True for 0 to 2pi. """
    if not bounded:
        return np.deg2rad(deg)
    return np.deg2rad(deg) % (2*np.pi)

def rad_2_deg(rad):
    """ Returns degree value from rad. Bounded=True for 0 to 2pi. """
    return np.rad2deg(rad)
