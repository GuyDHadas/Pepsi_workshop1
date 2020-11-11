import numpy as np
from math import *


def get_next_loc(current_x, current_y, theta, l_mean):
    """returns the next location of proton"""
    l = np.random.exponential(l_mean, 1)
    new_y = l * sin(theta) + current_x
    new_x = l * cos(theta) + current_y
    return new_x, new_y, l
